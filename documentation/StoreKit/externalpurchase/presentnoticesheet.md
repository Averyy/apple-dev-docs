# presentNoticeSheet()

**Framework**: StoreKit  
**Kind**: method

Presents a notice sheet from Apple that informs people before showing external purchases and determines whether your app can present external purchases.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
static func presentNoticeSheet() async throws -> ExternalPurchase.NoticeResult
```

## Mentions

- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)

#### Return Value

This returns [`ExternalPurchase.NoticeResult`](externalpurchase/noticeresult.md).

#### Discussion

This method is only available to apps with the [`com.apple.developer.storekit.external-purchase`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase) entitlement. For more information, see [`ExternalPurchase`](externalpurchase.md).

Call this method each time your app is ready to present an external purchase. To use this method, follow these steps:

1. Call [`canPresent`](externalpurchase/canpresent.md). If it’s `false`, don’t call [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md) and don’t show external purchases.
2. If [`canPresent`](externalpurchase/canpresent.md) is `true`, display buttons or other user-interface elements to enable deliberate user interaction. Then, in response to a deliberate user interaction such as tapping a button, call [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md) as shown below:

```swift
try await ExternalPurchase.presentNoticeSheet()
```

1. If the result is [`ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`](externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:).md) your app can show external purchases. Otherwise, you must not show external purchases.

> ❗ **Important**:  Record and use the token from the result to report to Apple the customer’s external purchases. For more information on reporting, see [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

 Record and use the token from the result to report to Apple the customer’s external purchases. For more information on reporting, see [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

This method throws a [`StoreKitError`](storekiterror.md) in any of the following conditions:

- Your app doesn’t have the [`com.apple.developer.storekit.external-purchase`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase) entitlement.
- Your app doesn’t have external purchases configured for the current App Store storefront; see [`SKExternalPurchase`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchase) and [`Storefront`](storefront.md).
- The current App Store storefront doesn’t support external purchases.
- The person is ineligible to make external purchases.
- A network or system error occurs.

This method also throws a [`StoreKitError`](storekiterror.md) if its functionality is unavailable for the following reasons:

- Your app is built with Mac Catalyst and you compile with an SDK earlier than iOS 17.4 or iPadOS 17.4.
- Your app is a compatible iPad or iPhone app running in macOS or visionOS and uses an SDK earlier than iOS 17.4 or iPadOS 17.4.

For apps compiled with SDKs earlier than iOS 17.4 or iPadOS 17.4, your app can show external purchases if the result is `ExternalPurchase.NoticeResult.continued`.

## See Also

- [static var canPresent: Bool](externalpurchase/canpresent.md)
  A Boolean value that indicates whether the app can successfully present the notice sheet to inform people about external purchases.
- [ExternalPurchase.NoticeResult](externalpurchase/noticeresult.md)
  The options available to people while viewing the external purchase notice sheet.
- [SKExternalPurchase](../BundleResources/Information-Property-List/SKExternalPurchase.md)
  A string array of country codes that indicates your app supports external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchase/presentnoticesheet())*