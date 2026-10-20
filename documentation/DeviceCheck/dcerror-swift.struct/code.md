# DCError.Code

**Framework**: DeviceCheck  
**Kind**: enum  
**Role**: Enumeration

DeviceCheck error codes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Code
```

```c
enum DCError : NSInteger;
```

## Topics

### Error codes
- [DCError.Code.featureUnsupported](./code/featureunsupported.md)
  DeviceCheck is unavailable on this device.
- [DCError.Code.invalidInput](./code/invalidinput.md)
  An error code that indicates when your app provides data that isn’t formatted correctly.
- [DCError.Code.invalidKey](./code/invalidkey.md)
  An error caused by a failed attempt to use the App Attest key.
- [DCError.Code.serverUnavailable](./code/serverunavailable.md)
  An error that indicates a failed attempt to contact the App Attest service during an attestation.
- [DCError.Code.unknownSystemFailure](./code/unknownsystemfailure.md)
  A failure has occurred, such as the failure to generate a token.
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

### Errors
- [struct DCError](../dcerror-swift.struct.md)
  A type that indicates when DeviceCheck encounters an error.
- [let DCErrorDomain: String](../dcerrordomain.md)
  The error domain for errors associated with DeviceCheck APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct/code)*