# presentNoticeSheet()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Presents a notice sheet from Apple that informs people of external purchases before showing them, and determines if your app can present external purchases

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

- [Receiving and decoding external purchase tokens](../receiving-and-decoding-external-purchase-tokens.md)

#### Return Value

This method returns [`ExternalPurchase.NoticeResult`](./noticeresult.md).

#### Discussion

This method is only available to apps with the [`com.apple.developer.storekit.external-purchase`](../../BundleResources/entitlements/com.apple.developer.storekit.external-purchase.md) entitlement. For more information, see [`ExternalPurchase`](../externalpurchase.md).

Call this method each time your app is ready to present an external purchase. To use this method, follow these steps:

1. Call [`canPresent`](./canpresent.md). If it’s `false`, don’t call [`presentNoticeSheet()`](./presentnoticesheet%28%29.md) and don’t show external purchases.
2. If [`canPresent`](./canpresent.md) is `true`, display buttons or other user-interface elements to enable deliberate user interaction. Then, in response to a deliberate user interaction such as tapping a button, call [`presentNoticeSheet()`](./presentnoticesheet%28%29.md) as shown below:

```swift
try await ExternalPurchase.presentNoticeSheet()
```

1. If the result is [`ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`](./noticeresult/continuedwithexternalpurchasetoken%28token%29.md) your app can show external purchases. Otherwise, you must not show external purchases.

> ❗ **Important**:  Record and use the token from the result to report to Apple the customer’s external purchases. For more information on reporting, see [External Purchase Server API](../../ExternalPurchaseServerAPI/ExternalPurchaseServerAPI.md).

This method throws a [`StoreKitError`](../storekiterror.md) in any of the following conditions:

- The current App Store storefront doesn’t support external purchases.
- The person is ineligible to make external purchases.
- Your app doesn’t have the necessary entitlement.
- Your app doesn’t configure external purchase for the current App Store storefront in [`SKExternalPurchase`](../../BundleResources/information-property-list/skexternalpurchase.md) when it has the [`com.apple.developer.storekit.external-purchase`](../../BundleResources/entitlements/com.apple.developer.storekit.external-purchase.md) entitlement.
- A network or system error occurs.

This method also throws a [`StoreKitError`](../storekiterror.md) if its functionality is unavailable for the following reasons:

- Your app is built with Mac Catalyst and you compile with an SDK earlier than iOS 17.4 or iPadOS 17.4.
- Your app is a compatible iPad or iPhone app running in macOS or visionOS and uses an SDK earlier than iOS 17.4 or iPadOS 17.4.

For apps compiled with SDKs earlier than iOS 17.4 or iPadOS 17.4, your app can show external purchases if the result is `ExternalPurchase.NoticeResult.continued`.

## See Also

### Offering an external purchase
- [static var canPresent: Bool](./canpresent.md)
  A Boolean value that indicates whether the app can successfully present the notice sheet to inform people about external purchases.
- [ExternalPurchase.NoticeResult](./noticeresult.md)
  The options available to people while viewing the external purchase notice sheet.
- [SKExternalPurchase](../../BundleResources/information-property-list/skexternalpurchase.md)
  A string array of country codes that indicates your app supports external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchase/presentnoticesheet())*