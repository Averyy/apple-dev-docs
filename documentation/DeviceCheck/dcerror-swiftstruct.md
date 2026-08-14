# DCError

**Framework**: DeviceCheck  
**Kind**: struct

A type that indicates when DeviceCheck encounters an error.

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
struct DCError
```

## Topics

### Errors
- [static var featureUnsupported: DCError.Code](dcerror-swift.struct/featureunsupported.md)
  DeviceCheck is not available on this device.
- [static var invalidInput: DCError.Code](dcerror-swift.struct/invalidinput.md)
  An error code that indicates when your app provides data that isn’t formatted correctly.
- [static var invalidKey: DCError.Code](dcerror-swift.struct/invalidkey.md)
  An error caused by a failed attempt to use the App Attest key.
- [static var serverUnavailable: DCError.Code](dcerror-swift.struct/serverunavailable.md)
  An error that indicates a failed attempt to contact the App Attest service during an attestation.
- [static var unknownSystemFailure: DCError.Code](dcerror-swift.struct/unknownsystemfailure.md)
  A failure has occurred, such as the failure to generate a token.
- [DCError.Code](dcerror-swift.struct/code.md)
  DeviceCheck error codes.
### Error information
- [static var errorDomain: String](dcerror-swift.struct/errordomain.md)
  The error domain for errors associated with DeviceCheck APIs.

## Relationships

### Conforms To
- [CustomNSError](../foundation/customnserror.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [DCError.Code](dcerror-swift.struct/code.md)
  DeviceCheck error codes.
- [let DCErrorDomain: String](dcerrordomain.md)
  The error domain for errors associated with DeviceCheck APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct)*