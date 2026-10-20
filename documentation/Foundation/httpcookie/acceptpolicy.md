# HTTPCookie.AcceptPolicy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Cookie acceptance policies implemented by the [`HTTPCookieStorage`](../httpcookiestorage.md) class.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum AcceptPolicy
```

```c
enum NSHTTPCookieAcceptPolicy : NSUInteger;
```

## Topics

### Policies
- [HTTPCookie.AcceptPolicy.always](./acceptpolicy/always.md)
  Accept all cookies.
- [HTTPCookie.AcceptPolicy.never](./acceptpolicy/never.md)
  Reject all cookies.
- [HTTPCookie.AcceptPolicy.onlyFromMainDocumentDomain](./acceptpolicy/onlyfrommaindocumentdomain.md)
  Accept cookies only from the main document domain.
### Initializers
- [init?(rawValue: UInt)](./acceptpolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/acceptpolicy)*