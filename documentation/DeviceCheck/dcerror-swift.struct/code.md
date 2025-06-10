# DCError.Code

**Framework**: DeviceCheck  
**Kind**: enum

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

## Topics

### Error codes
- [DCError.Code.featureUnsupported](dcerror-swift.struct/code/featureunsupported.md)
  DeviceCheck is unavailable on this device.
- [DCError.Code.invalidInput](dcerror-swift.struct/code/invalidinput.md)
  An error code that indicates when your app provides data that isn’t formatted correctly.
- [DCError.Code.invalidKey](dcerror-swift.struct/code/invalidkey.md)
  An error caused by a failed attempt to use the App Attest key.
- [DCError.Code.serverUnavailable](dcerror-swift.struct/code/serverunavailable.md)
  An error that indicates a failed attempt to contact the App Attest service during an attestation.
- [DCError.Code.unknownSystemFailure](dcerror-swift.struct/code/unknownsystemfailure.md)
  A failure has occurred, such as the failure to generate a token.
### Initializers
- [init?(rawValue: Int)](dcerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DCError](dcerror-swift.struct.md)
  A type that indicates when DeviceCheck encounters an error.
- [let DCErrorDomain: String](dcerrordomain.md)
  The error domain for errors associated with DeviceCheck APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct/code)*