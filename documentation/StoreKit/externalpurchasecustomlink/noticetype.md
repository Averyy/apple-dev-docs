# ExternalPurchaseCustomLink.NoticeType

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

The custom link out style that informs the type of disclosure notice to display.

**Availability**:
- iOS 18.1+ - Deprecated in 27.2
- iPadOS 18.1+ - Deprecated in 27.2
- Mac Catalyst 18.1+ - Deprecated in 27.2
- macOS 15.1+ - Deprecated in 27.2
- tvOS 18.1+ - Deprecated in 27.2
- visionOS 2.1+ - Deprecated in 27.2
- watchOS 11.1+ - Deprecated in 27.2

> **Deprecated**: Use `ExternalPurchaseType` instead.

## Declaration

```swift
enum NoticeType
```

## Overview

Provide a notice type value when you call [`showNotice(type:)`](./shownotice%28type%29.md).

## Topics

### Getting notice types
- [ExternalPurchaseCustomLink.NoticeType.browser](./noticetype/browser.md)
  A notice type that indicates your app displays external purchases in a destination of your choice.
- [ExternalPurchaseCustomLink.NoticeType.withinApp](./noticetype/withinapp.md)
  A notice type that indicates that you display the destination in a web view or native experience within the app.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated methods and values
- [static func showNotice(type: ExternalPurchaseCustomLink.NoticeType) async throws -> ExternalPurchaseCustomLink.NoticeResult](./shownotice%28type%29.md)
  Displays the system disclosure notice sheet and asks the customer whether to continue.
- [static func token(for: String) async throws -> ExternalPurchaseCustomLink.Token?](./token%28for%29-1fyo.md)
  Returns an external purchase token of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticetype)*