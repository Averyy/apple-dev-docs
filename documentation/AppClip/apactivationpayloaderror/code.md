# APActivationPayloadError.Code

**Framework**: App Clips  
**Kind**: enum

Error codes that an App Clip activation payload returns.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum Code
```

## Topics

### Error types
- [APActivationPayloadError.Code.doesNotMatch](apactivationpayloaderror/code/doesnotmatch.md)
  The provided URL doesn’t match the registered App Clip URL.
- [APActivationPayloadError.Code.disallowed](apactivationpayloaderror/code/disallowed.md)
  The user denied location access, or the source of the App Clip invocation wasn’t from an NFC tag or visual code.
### Initializers
- [init?(rawValue: Int)](apactivationpayloaderror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let APActivationPayloadErrorDomain: String](apactivationpayloaderrordomain.md)
  A string that identifies the activation payload’s error domain.
- [struct APActivationPayloadError](apactivationpayloaderror.md)
  An error that an App Clip activation payload returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/apactivationpayloaderror/code)*