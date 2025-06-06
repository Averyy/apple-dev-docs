# canPresent

**Framework**: StoreKit  
**Kind**: property

A Boolean value that indicates whether the app can successfully present the notice sheet to inform people about external purchases.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
static var canPresent: Bool { get async }
```

#### Discussion

Check this property, as shown below, to determine whether your app can successfully call [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md) to inform people before showing external purchases:

```swift
await externalPurchase.canPresent 
```

Check the value of this property again whenever the App Store storefront changes by using the [`updates`](storefront/updates.md) asynchronous sequence of [`Storefront`](storefront.md).

This property is `true` if all the following conditions are met:

- The current App Store storefront allows external purchase, and the person is eligible to make external purchases.
- Your app configures the [`com.apple.developer.storekit.external-purchase`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase) entitlement.
- Your app configures the country code for the current App Store storefront in [`SKExternalPurchase`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchase).

Otherwise, this property is `false`.

When this property is `false`, check [`canMakePayments`](appstore/canmakepayments.md) to determine whether your app can offer in-app purchases using the StoreKit [`In-App Purchase`](in-app-purchase.md) APIs. For more information, see [`canMakePayments`](appstore/canmakepayments.md).

## See Also

- [static func presentNoticeSheet() async throws -> ExternalPurchase.NoticeResult](externalpurchase/presentnoticesheet.md)
  Presents a notice sheet from Apple that informs people before showing external purchases and determines whether your app can present external purchases.
- [ExternalPurchase.NoticeResult](externalpurchase/noticeresult.md)
  The options available to people while viewing the external purchase notice sheet.
- [SKExternalPurchase](../BundleResources/Information-Property-List/SKExternalPurchase.md)
  A string array of country codes that indicates your app supports external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchase/canpresent)*