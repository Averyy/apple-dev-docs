# Adding support for Tap to Share to your app

**Framework**: ProximityReader

Request and share customer information on device.

#### Overview

With Tap to Share, merchants can use an iPhone to connect to a customer’s iPhone or device and exchange information. Your app can request information from customers for membership sign-up or ship-to-home purchases, share a customer’s shopping cart information, and allow them to check out with Apple Pay on their own iPhone. Your app uses the [`ProximityReader`](ProximityReader.md) framework to open a [`CustomerEngagementSession`](customerengagementsession.md) that allows the customer to connect. From that session you can request or share information with the customer.

> ❗ **Important**: Tap to Share is supported on iPhone 12 and later. Your app needs a Tap to Pay on iPhone entitlement and the ability to open a session by [`Adding support for Tap to Pay on iPhone to your app`](adding-support-for-tap-to-pay-on-iphone-to-your-app.md), or retrieve and use a [`PaymentCardReader.Token`](paymentcardreader/token.md) to initialize a [`CustomerEngagementSession`](customerengagementsession.md) and connect to a customer’s device. For more information on the Tap to Pay on iPhone entitlement, see [`Setting up Tap to Pay on iPhone`](setting-up-the-entitlement-for-tap-to-pay-on-iphone.md) and the Building support for your app section in [`Tap to Pay on iPhone`](https://developer.apple.comhttps://developer.apple.com/tap-to-pay/).

Before you get started, you need to add the Tap to Share capability to your project in Xcode, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

#### Create a Session and Connect to a Customers Device

When your app opens a screen in which a merchant  requires input from a customer, create a session that provides relevant merchant information. This configuration includes your region, currency, and privacy policy URL. You can include additional data, depending on your needs.

```swift
    
let config = CustomerEngagementSession.Configuration(
                currency: Locale.Currency("USD"),
                region: .unitedStates,
                storeName: "Oakbrook Mall", //Optional information.
                deviceName: "Emily", //Optional information.
                passTypeIdentifiers: ["pass.com.example.app1", "pass.com.example.app2"], //OPTIONAL
                privacyPolicyURL: URL(string: "https://www.example.com/privacy-policy")
            )

// Prepare the session object.           
let session = CustomerEngagementSession(configuration: config)            
```

You create the session using the [`open(using:)`](customerengagementsession/open(using:).md) method in your [`CustomerEngagementSession`](customerengagementsession.md). The [`events`](customerengagementsession/events.md) property provides an asynchronous stream of events that you can use to determine the state of the session and manage your UI.

To open the session, you need a valid Tap to Pay on iPhone payment token, or a valid Tap to Pay on iPhone session. If the session is already open, you can omit the token when calling [`open(using:)`](customerengagementsession/open(using:).md).

```swift
// Optionally listen for `AsyncStream` events.

let events = session.events
Task { @MainActor [weak self] in
    for await status in events {
        
        guard let self else { return }


        switch status {
            case .connected: 
                // Update the connection status.
            case .ready: 
                // The customer device is ready.
            case .disconnected: 
                // Clean up the session.
            case .closed: 
                // Perform final cleanup.
            @unknown default:
        }
    }
}

// Use an already open Tap to Pay on iPhone session to open the `CustomerEngagementSession`.
try await session.open()

// Send a request to the customer device.
try await checkInCustomer()
```

Catch any errors that happen during an open session and take appropriate action. For more information about possible errors, see [`CustomerEngagementSession.Error`](customerengagementsession/error.md).

> **Note**: Calling [`open(using:)`](customerengagementsession/open(using:).md) prepares the connection between you and the customer’s devices. When the devices are brought together, the [`open(using:)`](customerengagementsession/open(using:).md) completes. At that point, you can request information from the customer.

#### Request Information From a Customer

After your session is ready, use the appropriate method to request customer information. You can look up an existing customer account through an existing Wallet Pass and fallback to a secondary identifier like an email address by sending a  [`requestCustomerInfo(for:fields:message:)`](customerengagementsession/requestcustomerinfo(for:fields:message:).md).

The example below shows how a merchant might accept a Wallet Pass or an email address as a form of identification for looking up a customer account.

```swift
func checkIn() async throws {

    // Ask the customer for a Wallet Pass, or fall back to an email address.
    let customerInfo = try await session.requestCustomerInfo(for: .checkin, 
        fields: [.pass, .emailAddress])
            
    // Use Pass information or other shared info to look up the customer account.
    let customerAccount: YourCustomerAccount?
    if let barcode = customerInfo.barcodeMessage {
        customerAccount = lookupMember(barcode)
    } else if let email = customerInfo.emailAddress {
        customerAccount = lookupMember(using: email)
    }
}

func addShippingAddress() async throws {

    // Ask the customer for their shipping address. This includes name, email, and phone number
    let address = try await session.requestAddress(for: .shipping,
        fields: [.emailAddress, .phoneNumber])

    // Add shipping information to your customer's order.
    addShippingToCustomerOrder(address)
}

func createCustomerAccount() async throws {


    // Ask the customer for their name, email, phone number, and marketing preferences.
    let signup = try await session.requestSignup(for: .membership,
        fields: [.emailAddress, .phoneNumber],
        emailConsent: CustomerEngagementSession.ConsentOption.visible,
        smsConsent: CustomerEngagementSession.ConsentOption.visible,
        termsAndConditions: markdownFormattedTermsAndCondition )

    // Create a new membership account.
    createAMembershipAccount(signup)
}
```

#### Share a Shopping Cart

At any point during the session, you can share a shopping cart with the customer by creating a [`CustomerEngagement.ShoppingCart`](customerengagement/shoppingcart.md) and using the [`updateShoppingCart(_:)`](customerengagementsession/updateshoppingcart(_:).md) method. Use the same method to repopulate the shopping cart when making updates. The shopping cart is stateless, so make sure to include the full shopping cart every update. You can also choose to share an empty shopping cart in the background as a placeholder throughout the session.

The following example shows how to share a shopping cart with a customer:

```swift
    
// Initiate a shopping cart by choosing items.
func populateShoppingCart() -> ShoppingCartToken {

    let items: [CustomerEngagement.ShoppingCart.Item]
    let summary: CustomerEngagement.ShoppingCart.Summary

    // Create a shopping cart.
    items = [
        // The item's unique identifier. This ensures smooth animation on the user device. 
        .init(id: "HRSP-M-UN-11-001", 
            name: "Hair Spray",
            quantity: 4,
            totalPrice: 20.00,
            totalAdjustedPrice: 15.00,
            descriptions: ["Unscented, 11 oz", "Buy 3 Get 1 Free Offer"],
            details: ["This item cannot be shipped."]
        )
    ]

    summary = .init(
        summaryLines: [
        .init(label: "Subtotal", value: 15.00),
        .init(label: "Coupon Code: NY2OFF", value: -2.00),
        .init(label: "Shipping", value: "Free"),
        .init(label: "Tax", value: "10%")
        ],
        footer: "Thank you for shopping with us.",
        total: 14.30
    )
    
    let cart = CustomerEngagement.ShoppingCart(items: items, summary: summary)
    try await let shoppingCartToken = session.updateShoppingCart(cart)
    
    return shoppingCartToken
}
```

In addition to the [`updateShoppingCart(_:)`](customerengagementsession/updateshoppingcart(_:).md), you can update the customer screen using the [`updateStatus(_:)`](customerengagementsession/updatestatus(_:).md) method. This method allows you to indicate a screen state when there aren’t any active request forms on the customer screen. For example, when a customer has completed their payment, you can update the customer screen with [`CustomerEngagement.Status.paymentCompleted`](customerengagement/status/paymentcompleted.md).

#### Request an Apple Pay Payment

Tap to Share allows the customer to pay using an Apple Pay payment sheet. If the customer uses a [`CustomerEngagementSession.PeerClientType.localWireless`](customerengagementsession/peerclienttype/localwireless.md) connection, indicating they’re on a compatible iOS version, prompt them to complete a full or partial payment of the shopping cart using Apple Pay. If the customer hasn’t set up Apple Pay on their device or chooses not to use Apple Pay, [`requestPayment(for:using:delegate:)`](customerengagementsession/requestpayment(for:using:delegate:).md) returns `false` and you must use another payment method to receive the payment from the customer.

> **Note**: The Apple Pay option can only be displayed on a shopping cart view using a [`CustomerEngagement.ShoppingCartToken`](customerengagement/shoppingcarttoken.md) that you get when you share a shopping cart to a customer’s device. Without the token, other payment methods like [`Adding support for Tap to Pay on iPhone to your app`](adding-support-for-tap-to-pay-on-iphone-to-your-app.md) can be used.

The example below shows how a merchant might use Apple Pay to request a payment from a customer:

```swift
    
// If the host app supports Apple Pay, ask the customer to select a payment option.

func payWithApplePay(shoppingCartToken: ShoppingCartToken) {
    
    // The merchant uses the existing Apple Pay API, except for the new `prepareRemotePayment()`.
    
    let fare = PKPaymentSummaryItem(label: "Minimum Fare", amount: NSDecimalNumber(string: "9.99"), type: .final)
    let tax = PKPaymentSummaryItem(label: "Tax", amount: NSDecimalNumber(string: "1.00"), type: .final)
    let total = PKPaymentSummaryItem(label: "Total", amount: NSDecimalNumber(decimal: total), type: .final)
    paymentSummaryItems = [fare, tax, total]

    let paymentRequest = PKPaymentRequest()
    paymentRequest.paymentSummaryItems = paymentSummaryItems
    paymentRequest.currencyCode = "USD"
    paymentRequest.countryCode = "US"
    paymentRequest.supportedNetworks = [.amex, .discover, .masterCard, .visa]
    paymentRequest.merchantCapabilities = .threeDSecure
    paymentRequest.merchantIdentifier = "merchant.com.example.posapp1"

    do {
        if try await session.requestPayment(for: shoppingCartToken, 
                                            using: paymentRequest,
                                            delegate: pkPaymentAuthorizationControllerDelegate) {
            log("payment sheet presented successfully")
        } else {
            // If the customer selected a non-Apple Pay option or they haven't set up Apple Pay, proceed with a different payment method.
            tapToPay()
        }
    } catch {
        log("failed to present payment sheet")
    }
}

// Check for payment authorization. 
func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, 
    didAuthorizePayment payment: PKPayment, 
    handler completion: @escaping (PKPaymentAuthorizationResult) -> Void) {
    
    log("success, process PKPayment")
    // Check for errors. 
    let errors = [Error]()
    completion(PKPaymentAuthorizationResult(status: .success, errors: errors))

}

func paymentAuthorizationControllerDidFinish(_ controller: PKPaymentAuthorizationController) {
    log("sheet dismissed")
}
```

#### Add a Wallet Pass

If the merchant supports loyalty or membership Wallet Passes, you can use the [`addPass(_:)`](customerengagementsession/addpass(_:).md) method to allow the customer to add your pass to their Wallet. For example, after a customer successfully signs up for a membership program, your app can obtain a pass from the merchant and send it to the customer’s Wallet. Make sure to create and sign the `.pkpass` data file.

#### End a Session with a Customer

To provide the best customer experience,  programmatically end the connection when your workflow completes. For example, when a customer finishes a payment, use the [`close()`](customerengagementsession/close().md) method to end the session.

## See Also

- [enum CustomerEngagement](customerengagement.md)
  An enumeration of the shared data between the merchant and customer.
- [class CustomerEngagementSession](customerengagementsession.md)
  The object you use to share and request customer information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-share-to-your-app)*