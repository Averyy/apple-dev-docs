# ExternalPurchaseCustomLink.NoticeResult

**Framework**: StoreKit  
**Kind**: enum

The result of showing the disclosure notice.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
enum NoticeResult
```

#### Overview

This value is the result of calling [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md).

If the value is [`ExternalPurchaseCustomLink.NoticeResult.continued`](externalpurchasecustomlink/noticeresult/continued.md), the customer choses to continue and your app can offer custom links for external purchases. Otherwise, don’t continue.

## Topics

### Getting notice results
- [ExternalPurchaseCustomLink.NoticeResult.cancelled](externalpurchasecustomlink/noticeresult/cancelled.md)
  The customer chooses to cancel; don’t offer external purchases.
- [ExternalPurchaseCustomLink.NoticeResult.continued](externalpurchasecustomlink/noticeresult/continued.md)
  The customer chooses to continue; the app can offer external purchases.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func showNotice(type: ExternalPurchaseCustomLink.NoticeType) async throws -> ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/shownotice(type:).md)
  Displays the system disclosure notice sheet and asks the customer whether to continue.
- [ExternalPurchaseCustomLink.NoticeType](externalpurchasecustomlink/noticetype.md)
  The custom link out style that informs the type of disclosure notice to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticeresult)*