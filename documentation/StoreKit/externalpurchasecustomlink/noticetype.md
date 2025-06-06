# ExternalPurchaseCustomLink.NoticeType

**Framework**: StoreKit  
**Kind**: enum

The custom link out style that informs the type of disclosure notice to display.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
enum NoticeType
```

#### Overview

Provide a notice type value when you call [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md).

## Topics

### Getting notice types
- [ExternalPurchaseCustomLink.NoticeType.browser](externalpurchasecustomlink/noticetype/browser.md)
  A notice type that indicates you display external purchases in a destination outside of the app, which can be an alternative marketplace, another app, or a website.
- [ExternalPurchaseCustomLink.NoticeType.withinApp](externalpurchasecustomlink/noticetype/withinapp.md)
  A notice type that indicates that you display the destination in a web view within the app.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func showNotice(type: ExternalPurchaseCustomLink.NoticeType) async throws -> ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/shownotice(type:).md)
  Displays the system disclosure notice sheet and asks the customer whether to continue.
- [ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/noticeresult.md)
  The result of showing the disclosure notice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticetype)*