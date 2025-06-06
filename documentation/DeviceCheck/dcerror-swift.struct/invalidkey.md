# invalidKey

**Framework**: DeviceCheck  
**Kind**: property

An error caused by a failed attempt to use the App Attest key.

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
static var invalidKey: DCError.Code { get }
```

#### Discussion

You receive this error if something goes wrong with generating, retrieving, or using an App Attest cryptographic key, when:

- You call [`attestKey(_:clientDataHash:completionHandler:)`](dcappattestservice/attestkey(_:clientdatahash:completionhandler:).md) for a key that’s already been attested.
- You call [`generateAssertion(_:clientDataHash:completionHandler:)`](dcappattestservice/generateassertion(_:clientdatahash:completionhandler:).md) with an unattested key.
- The App Attest service rejects the key.

## See Also

- [static var featureUnsupported: DCError.Code](dcerror-swift.struct/featureunsupported.md)
  DeviceCheck is not available on this device.
- [static var invalidInput: DCError.Code](dcerror-swift.struct/invalidinput.md)
  An error code that indicates when your app provides data that isn’t formatted correctly.
- [static var serverUnavailable: DCError.Code](dcerror-swift.struct/serverunavailable.md)
  An error that indicates a failed attempt to contact the App Attest service during an attestation.
- [static var unknownSystemFailure: DCError.Code](dcerror-swift.struct/unknownsystemfailure.md)
  A failure has occurred, such as the failure to generate a token.
- [DCError.Code](dcerror-swift.struct/code.md)
  DeviceCheck error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct/invalidkey)*