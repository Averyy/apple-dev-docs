# ExternalPurchase

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration that enables qualifying apps to offer external purchases within the app.

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
enum ExternalPurchase
```

## Overview

This functionality is only available to and required by apps with the [`com.apple.developer.storekit.external-purchase`](../BundleResources/entitlements/com.apple.developer.storekit.external-purchase.md) entitlement. For more information, see:

- [Distributing apps using alternative payment providers in the European Union](https://developer.apple.com/go/?id=storekit-external-purchase-eu)
- [Distributing dating apps in the Netherlands](https://developer.apple.com/support/storekit-external-entitlement/)
- [Distributing apps using a third-party payment provider in South Korea](https://developer.apple.com/support/storekit-external-entitlement-kr/)

> **Note**:  You must check [`canMakePayments`](./appstore/canmakepayments.md) before calling the External Purchase APIs. If [`canMakePayments`](./appstore/canmakepayments.md) is `false`, don’t call the [`ExternalPurchaseLink`](./externalpurchaselink.md) or [`ExternalPurchase`](./externalpurchase.md) APIs.

## Topics

### Offering an external purchase
- [static var canPresent: Bool](./externalpurchase/canpresent.md)
  A Boolean value that indicates whether the app can successfully present the notice sheet to inform people about external purchases.
- [static func presentNoticeSheet() async throws -> ExternalPurchase.NoticeResult](./externalpurchase/presentnoticesheet%28%29.md)
  Presents a notice sheet from Apple that informs people of external purchases before showing them, and determines if your app can present external purchases
- [ExternalPurchase.NoticeResult](./externalpurchase/noticeresult.md)
  The options available to people while viewing the external purchase notice sheet.
- [SKExternalPurchase](../BundleResources/information-property-list/skexternalpurchase.md)
  A string array of country codes that indicates your app supports external purchases.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Implementing alternative payment service providers in the EU and South Korea
- [com.apple.developer.storekit.external-purchase](../BundleResources/entitlements/com.apple.developer.storekit.external-purchase.md)
  A Boolean value that indicates whether your app can offer external purchases.
- [SKExternalPurchase](../BundleResources/information-property-list/skexternalpurchase.md)
  A string array of country codes that indicates your app supports external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchase)*