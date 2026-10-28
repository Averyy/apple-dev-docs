# DCError.Code.invalidKey

**Framework**: DeviceCheck  
**Kind**: case  
**Role**: Case

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
case invalidKey
```

```c
DCErrorInvalidKey
```

## Discussion

You receive this error if something goes wrong with generating, retrieving, or using an App Attest cryptographic key, when:

- You call [`attestKey(_:clientDataHash:completionHandler:)`](../../dcappattestservice/attestkey%28_,clientdatahash,completionhandler%29.md) for a key that’s already been attested.
- You call [`generateAssertion(_:clientDataHash:completionHandler:)`](../../dcappattestservice/generateassertion%28_,clientdatahash,completionhandler%29.md) with an unattested key.
- The App Attest service cannot enforce the key access control policy on macOS.
- The App Attest service rejects the key.

## See Also

### Error codes
- [DCError.Code.featureUnsupported](./featureunsupported.md)
  DeviceCheck is unavailable on this device.
- [DCError.Code.invalidInput](./invalidinput.md)
  An error code that indicates when your app provides data that isn’t formatted correctly.
- [DCError.Code.serverUnavailable](./serverunavailable.md)
  An error that indicates a failed attempt to contact the App Attest service during an attestation.
- [DCError.Code.unknownSystemFailure](./unknownsystemfailure.md)
  A failure has occurred, such as the failure to generate a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct/code/invalidkey)*