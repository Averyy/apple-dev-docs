# unknownSystemFailure

**Framework**: DeviceCheck  
**Kind**: property  
**Role**: Type Property

A failure has occurred, such as the failure to generate a token.

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
static var unknownSystemFailure: DCError.Code { get }
```

## See Also

### Errors
- [static var featureUnsupported: DCError.Code](./featureunsupported.md)
  DeviceCheck is not available on this device.
- [static var invalidInput: DCError.Code](./invalidinput.md)
  An error code that indicates when your app provides data that isn’t formatted correctly.
- [static var invalidKey: DCError.Code](./invalidkey.md)
  An error caused by a failed attempt to use the App Attest key.
- [static var serverUnavailable: DCError.Code](./serverunavailable.md)
  An error that indicates a failed attempt to contact the App Attest service during an attestation.
- [DCError.Code](./code.md)
  DeviceCheck error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct/unknownsystemfailure)*