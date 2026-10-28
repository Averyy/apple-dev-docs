# ExternalPurchaseCustomLink.NoticeResult

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

The result of showing the disclosure notice.

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
enum NoticeResult
```

## Overview

This value is the result of calling [`showNotice(type:)`](./shownotice%28type%29.md).

If the value is [`ExternalPurchaseCustomLink.NoticeResult.continued`](./noticeresult/continued.md), the customer choses to continue and your app can communicate and promote offers for purchase in a distribution channel of your choice. Otherwise, don’t continue.

## Topics

### Getting notice results
- [ExternalPurchaseCustomLink.NoticeResult.cancelled](./noticeresult/cancelled.md)
  The customer chooses to cancel; don’t offer external purchases.
- [ExternalPurchaseCustomLink.NoticeResult.continued](./noticeresult/continued.md)
  The customer chooses to continue; the app can offer external purchases.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Displaying the disclosure sheet
- [static func showNotice(for: ExternalPurchaseCustomLink.ExternalPurchaseType) async throws -> ExternalPurchaseCustomLink.NoticeResult](./shownotice%28for%29.md)
  Displays the system disclosure notice sheet for a custom link type and asks the customer whether to continue.
- [ExternalPurchaseCustomLink.ExternalPurchaseType](./externalpurchasetype.md)
  Values that represent the types of external purchase an app can perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticeresult)*