# APActivationPayloadError

**Framework**: App Clips  
**Kind**: struct

An error that an App Clip activation payload returns.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
struct APActivationPayloadError
```

## Topics

### Getting information about the error
- [static var errorDomain: String](apactivationpayloaderror/errordomain.md)
### Interpreting errors
- [static var doesNotMatch: APActivationPayloadError.Code](apactivationpayloaderror/doesnotmatch.md)
  The provided URL doesn’t match the invocation URL you registered for the App Clip.
- [static var disallowed: APActivationPayloadError.Code](apactivationpayloaderror/disallowed.md)
  The user denied location access, or the source of the App Clip invocation wasn’t an NFC tag or visual code.
- [APActivationPayloadError.Code](apactivationpayloaderror/code.md)
  Error codes that an App Clip activation payload returns.

## Relationships

### Conforms To
- [CustomNSError](../foundation/customnserror.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let APActivationPayloadErrorDomain: String](apactivationpayloaderrordomain.md)
  A string that identifies the activation payload’s error domain.
- [APActivationPayloadError.Code](apactivationpayloaderror/code.md)
  Error codes that an App Clip activation payload returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/apactivationpayloaderror)*