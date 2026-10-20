# DCError.Code.serverUnavailable

**Framework**: DeviceCheck  
**Kind**: case  
**Role**: Case

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
case serverUnavailable
```

```c
DCErrorServerUnavailable
```

#### Discussion

You receive this error when you call [`attestKey(_:clientDataHash:completionHandler:)`](../../dcappattestservice/attestkey%28_,clientdatahash,completionhandler%29.md) and the framework isn’t able to complete the attestation. If you receive this error, try the attestation again later using the same key and the same value for the `clientDataHash` parameter. Retrying with the same inputs helps to preserve the risk metric for a given device.

## See Also

### Error codes
- [DCError.Code.featureUnsupported](./featureunsupported.md)
  DeviceCheck is unavailable on this device.
- [DCError.Code.invalidInput](./invalidinput.md)
  An error code that indicates when your app provides data that isn’t formatted correctly.
- [DCError.Code.invalidKey](./invalidkey.md)
  An error caused by a failed attempt to use the App Attest key.
- [DCError.Code.unknownSystemFailure](./unknownsystemfailure.md)
  A failure has occurred, such as the failure to generate a token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct/code/serverunavailable)*