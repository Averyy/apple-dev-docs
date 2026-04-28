# ExternalPurchaseCustomLink

**Framework**: StoreKit  
**Kind**: enum

An enumeration that enables qualifying apps to offer custom links for external purchases and use alternative payment service providers.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
enum ExternalPurchaseCustomLink
```

## Mentions

- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)
- [Testing transactions that use custom link tokens](testing-transactions-that-use-custom-link-tokens.md)

#### Overview

This functionality is only available to apps with the any of the following entitlements:

- [`com.apple.developer.storekit.custom-purchase-link.allowed-regions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions)
- [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link)
- [`com.apple.developer.storekit.external-purchase-link-streaming`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link-streaming)

For more information, see:

- [`Communication and promotion of offers on the App Store in the EU`](https://developer.apple.comhttps://developer.apple.com/support/communication-and-promotion-of-offers-on-the-app-store-in-the-eu/)
- [`Distributing music streaming apps in the EEA that provide an external purchase link`](https://developer.apple.comhttps://developer.apple.com/support/music-streaming-services-entitlement-eea/)
- [`Payment options on the App Store in Japan`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-japan)

##### Implement External Purchase for Apps Available in Japan

If your account receives the StoreKit External Custom Purchase Link Regions entitlement, in Japan your app can use the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to implement external purchases starting in iOS 26.2.  To use this API, complete the following steps:

- Configure the [`com.apple.developer.storekit.custom-purchase-link.allowed-regions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions) entitlement for your app.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md) API to determine whether the API is available at runtime. If the value is `false`, don’t continue to use this API. For more information, see  [`isEligible`](externalpurchasecustomlink/iseligible.md).
- Starting in iOS 26.4, call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function before every potential transaction to request external purchase tokens, using the token types `IN_APP` or `LINK_OUT`. For more information, see [`token(for:)`](externalpurchasecustomlink/token(for:).md).
- Before routing customers to external purchase options, display an in-app disclosure sheet that lets people know they’ll be transacting with you and not Apple. For more information, including downloadable resources, see the “In-app disclosure sheet” section of [`Payment options on the App Store in Japan`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-japan).
- Starting in iOS 26.4, report the external purchase tokens and the transactions associated with the tokens using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI). Otherwise, report transactions as indicated in [`Payment options on the App Store in Japan`](https://developer.apple.comhttps://developer.apple.com/support/payment-options-on-the-app-store-in-japan).

##### Implement External Purchase for Apps Available in the European Union Eu

If your account receives the StoreKit External Purchase Link (EU) entitlement or the StoreKit External Custom Purchase Link Regions entitlement, in the EU your app can use the `ExternalPurchaseCustomLink` API to implement external purchases. To use this API, complete the following steps:

- Depending on the entitlement you receive, configure the [`com.apple.developer.storekit.custom-purchase-link.allowed-regions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions) entitlement for your app, or configure the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link) entitlement and the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key, including the country code for each permitted region where your app implements external purchases.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the `ExternalPurchaseCustomLink` API to determine whether the API is available at runtime. If the value is false, don’t continue to use this API. See [`isEligible`](externalpurchasecustomlink/iseligible.md) for more details.
- At launch and before every potential transaction, call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function to request the external purchase tokens, using the token types `ACQUISITION` and `SERVICES`. Associate these tokens with a customer account on your server.
- Call the [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md) function after a deliberate customer interaction, such as tapping a button, that can lead to a potential external purchase.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

For information about testing in the sandbox environment, see [`Testing transactions that use custom link tokens`](testing-transactions-that-use-custom-link-tokens.md).

##### Implement External Purchase for Music Streaming Apps in the European Economic Area Eea

If your account receives the Music Streaming Services EEA entitlement, in the EEA your music-streaming app can use the `ExternalPurchaseCustomLink` API to implement external purchases. To use this API, complete the following steps:

- Configure the [`com.apple.developer.storekit.external-purchase-link-streaming`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link-streaming) entitlement for your app and the [`SKExternalPurchaseLinkStreamingRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLinkStreamingRegions) property list key, providing the country code for each permitted region where your app implements external purchases.
- Check the [`isEligible`](externalpurchasecustomlink/iseligible.md) property of the `ExternalPurchaseCustomLink` API to determine whether external purchase is available at runtime. If the value is false, don’t continue to use this API. See [`isEligible`](externalpurchasecustomlink/iseligible.md) for more details.
- At launch and before every potential transaction, call the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function to request the external purchase tokens, using the token types `ACQUISITION` and `SERVICES`. Associate these tokens with a customer account on your server.
- Call the [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md) function after a deliberate customer interaction, such as tapping a button, that can lead to a potential external purchase.
- From your server, report the external purchase tokens and the transactions associated with the tokens by using the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

##### Check Eligibility and Request Tokens for Apps Available in the Eu

When your app launches, check whether its eligible to use the `ExternalPurchaseCustomLink` API. For more information, see [`isEligible`](externalpurchasecustomlink/iseligible.md) and [`canMakePayments`](appstore/canmakepayments.md).

If your app is eligible, request both the `ACQUISITION` and `SERVICES` external purchase tokens. Associate and store these tokens with a customer account on your server. Use the tokens to report transactions to Apple.

The following example code shows how to check for eligibility and request custom link tokens:

```swift
// Ensure the app is eligible to use the external purchase custom link API.
guard await ExternalPurchaseCustomLink.isEligible else { return }

// Declare the tokens and the token types.
var tokens: [String : String] = [:]
let tokenTypes = ["ACQUISITION", "SERVICES"]

// Request the tokens.
for tokenType in tokenTypes {
    do {
        let token = try await ExternalPurchaseCustomLink.token(for: tokenType)
        if let token {
            tokens[tokenType] = token.value
        }
    }
    catch {
        // Failed to get a token of type `tokenType`.
        // Add your code to handle errors.
    }
}

// Add your code to manage the tokens, for example to associate them
// with a customer account on your server.
```

##### Display the Disclosure Notice Before Displaying External Purchases

The following SwiftUI code example shows how to check for eligibility, and then show the disclosure notice to determine whether to continue to display external purchases:

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
  A Boolean value that indicates at runtime whether the app can use this API for external purchases.
### Getting external purchase tokens
- [static func token(for: String) async throws -> ExternalPurchaseCustomLink.Token?](externalpurchasecustomlink/token(for:).md)
  Requests an external purchase token of the specified type.
- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  A token you use with the External Purchase custom link API.
- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)
  Receive tokens for external purchases that you use to report transactions to Apple.
### Displaying the disclosure sheet
- [static func showNotice(type: ExternalPurchaseCustomLink.NoticeType) async throws -> ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/shownotice(type:).md)
  Displays the system disclosure notice sheet and asks the customer whether to continue.
- [ExternalPurchaseCustomLink.NoticeType](externalpurchasecustomlink/noticetype.md)
  The custom link out style that informs the type of disclosure notice to display.
- [ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/noticeresult.md)
  The result of showing the disclosure notice.
### Testing external purchase transactions
- [Testing transactions that use custom link tokens](testing-transactions-that-use-custom-link-tokens.md)
  Recognize custom link tokens that your app receives in the sandbox testing environment, and use them to test reporting transactions.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ExternalPurchaseCustomLink.Token](externalpurchasecustomlink/token.md)
  A token you use with the External Purchase custom link API.
- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](../BundleResources/Entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md)
  An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-purchase-link](../BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link.md)
  A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseCustomLinkRegions](../BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions.md)
  An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
- [Testing transactions that use custom link tokens](testing-transactions-that-use-custom-link-tokens.md)
  Recognize custom link tokens that your app receives in the sandbox testing environment, and use them to test reporting transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink)*