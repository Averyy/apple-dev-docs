# ExternalPurchaseCustomLink

**Framework**: StoreKit  
**Kind**: enum

Enables qualifying apps to offer custom links for external purchases.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
enum ExternalPurchaseCustomLink
```

#### Overview

This functionality is only available to apps with the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link) entitlement. For more information, see:

- [`Using alternative payment options on the App Store in the European Union`](https://developer.apple.comhttps://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu/)
- [`Distributing music streaming apps in the EEA that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/support/music-streaming-services-entitlement-eea/)

##### Support External Purchases with Custom Links in Your App

If your account receives the StoreKit External Purchase Link entitlement, implement the following to offer custom links for external purchases:

- Configure the entitlement for your app. For more information, see [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link).
- Configure the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key. Include the country code for each permitted region where your app offers external purchase custom links.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) type to determine whether external purchase is available.
- At launch, call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function to request the external purchase tokens, using the token types `ACQUISITION` and `SERVICES`. Associate these tokens with a customer account on your server.
- Call the [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md) function after a deliberate customer interaction, such as tapping a button, and before linking out to external purchases.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

##### Check Eligibility and Request Tokens When the App Launches

When your app launches, check whether its eligible to use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API. For more information, see [`isEligible`](externalpurchasecustomlink/iseligible.md) and [`canMakePayments`](appstore/canmakepayments.md).

If your app is eligible, request both the `ACQUISITION` and `SERVICES` external purchase tokens. Associate and store these tokens with a customer account on your server. Use the tokens to report transactions to Apple.

The following example code shows how to check for eligibility and request tokens:

```swift
// Ensure the app is eligible to use the external purchase custom link API.
guard await ExternalPurchaseCustomLink.isEligible else { return }

// Declare the tokens and the token types.
var tokens: [String : String] = [:]
let tokenTypes = ["ACQUISITION", "SERVICES"]

// Request the tokens.
for tokenType in tokenTypes {
    do {
        tokens[tokenType] = try await ExternalPurchaseCustomLink.token(for: tokenType)
    }
    catch {
        // Failed to get a token of type `tokenType`.
        // Add your code to handle errors.
    }
}

// Add your code to manage the tokens, for example to associate them with
// a customer account on your server. 
```

##### Display the Disclosure Notice Before Presenting Custom Links for External Purchases

The following SwiftUI code example shows how to check for eligibility, and then show the disclosure notice to determine whether to continue to offer external purchases:

```swift
struct MyView: View {

    func openStore() async {
        guard await ExternalPurchaseCustomLink.isEligible else {
            return
        }
        // Show the disclosure notice.
        do {
            let result = try await ExternalPurchaseCustomLink.showNotice(type: .withinApp)
            guard case .continued = result else {
                // Customer chooses not to continue. Don't display external purchases.
                return
            }
            // Customer chooses to continue. 
            // Proceed with the custom link out and offer external purchases...
        }
        catch {
            // Add error handling here... 
        }
    }

    var body: some View {
        Button("Open store") {
            Task { await openStore() }
        }
    }
}
```

## Topics

### Checking eligibility
- [static var isEligible: Bool](externalpurchasecustomlink/iseligible.md)
  A Boolean value that indicates at runtime whether the app can use this API to offer custom links for external purchases.
### Getting external purchase tokens
- [static func token(for: String) async throws -> ExternalPurchaseCustomLink.Token?](externalpurchasecustomlink/token(for:).md)
  Requests an external purchase token of the specified type.
- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  An external purchase token for use with custom links.
### Displaying the disclosure sheet
- [static func showNotice(type: ExternalPurchaseCustomLink.NoticeType) async throws -> ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/shownotice(type:).md)
  Displays the system disclosure notice sheet and asks the customer whether to continue.
- [ExternalPurchaseCustomLink.NoticeType](externalpurchasecustomlink/noticetype.md)
  The custom link out style that informs the type of disclosure notice to display.
- [ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/noticeresult.md)
  The result of showing the disclosure notice.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  An external purchase token for use with custom links.
- [com.apple.developer.storekit.external-purchase-link](../BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseCustomLinkRegions](../BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions.md)
  An array of country code strings that indicate the regions where your app supports custom links for external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink)*