# ExternalPurchase.NoticeResult

**Framework**: StoreKit  
**Kind**: enum

The options available to people while viewing the external purchase notice sheet.

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
enum NoticeResult
```

#### Overview

These values return when your app calls [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md).

## Topics

### Getting notice sheet results
- [ExternalPurchase.NoticeResult.cancelled](externalpurchase/noticeresult/cancelled.md)
  Describes when people chose to cancel and not view external purchases.
- [ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)](externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:).md)
  Describes when people chose to continue to view external purchases, and provides the external purchase token.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var canPresent: Bool](externalpurchase/canpresent.md)
  A Boolean value that indicates whether the app can successfully present the notice sheet to inform people about external purchases.
- [static func presentNoticeSheet() async throws -> ExternalPurchase.NoticeResult](externalpurchase/presentnoticesheet.md)
  Presents a notice sheet from Apple that informs people of external purchases before showing them, and determines if your app can present external purchases
- [SKExternalPurchase](../BundleResources/Information-Property-List/SKExternalPurchase.md)
  A string array of country codes that indicates your app supports external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchase/noticeresult)*