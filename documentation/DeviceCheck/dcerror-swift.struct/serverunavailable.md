# serverUnavailable

**Framework**: DeviceCheck  
**Kind**: property

An error that indicates a failed attempt to contact the App Attest service during an attestation.

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
static var serverUnavailable: DCError.Code { get }
```

## Mentions

- [Establishing your app’s integrity](establishing-your-app-s-integrity.md)

#### Discussion

You receive this error when you call [`attestKey(_:clientDataHash:completionHandler:)`](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md) and the framework isn’t able to complete the attestation. If you receive this error, try the attestation again later using the same key and the same value for the `clientDataHash` parameter. Retrying with the same inputs helps to preserve the risk metric for a given device.

## See Also

- [static var featureUnsupported: DCError.Code](dcerror-swift.struct/featureunsupported.md)
  DeviceCheck is not available on this device.
- [static var invalidInput: DCError.Code](dcerror-swift.struct/invalidinput.md)
  An error code that indicates when your app provides data that isn’t formatted correctly.
- [static var invalidKey: DCError.Code](dcerror-swift.struct/invalidkey.md)
  An error caused by a failed attempt to use the App Attest key.
- [static var unknownSystemFailure: DCError.Code](dcerror-swift.struct/unknownsystemfailure.md)
  A failure has occurred, such as the failure to generate a token.
- [DCError.Code](dcerror-swift.struct/code.md)
  DeviceCheck error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct/serverunavailable)*