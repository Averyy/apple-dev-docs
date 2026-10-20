# APActivationPayloadError.Code

**Framework**: App Clips  
**Kind**: enum  
**Role**: Enumeration

Error codes that an App Clip activation payload returns.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum Code
```

```c
enum APActivationPayloadErrorCode : NSInteger;
```

## Topics

### Error types
- [APActivationPayloadError.Code.doesNotMatch](./code/doesnotmatch.md)
  The provided URL doesn’t match the registered App Clip URL.
- [APActivationPayloadError.Code.disallowed](./code/disallowed.md)
  The user denied location access, or the source of the App Clip invocation wasn’t from an NFC tag or visual code.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Understanding errors
- [let APActivationPayloadErrorDomain: String](../apactivationpayloaderrordomain.md)
  A string that identifies the activation payload’s error domain.
- [struct APActivationPayloadError](../apactivationpayloaderror.md)
  An error that an App Clip activation payload returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/apactivationpayloaderror/code)*