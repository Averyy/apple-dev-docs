# PKPassKitError.Code.invalidSignature

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Invalid pass signature.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case invalidSignature
```

```c
PKInvalidSignature
```

## Discussion

For example, the pass type identifier in the certificate and the pass do not match, or the certificate has expired or was revoked.

## See Also

### Error codes
- [PKPassKitError.Code.unknownError](./unknownerror.md)
  Unknown error.
- [PKPassKitError.Code.invalidDataError](./invaliddataerror.md)
  Invalid pass data.
- [PKPassKitError.Code.unsupportedVersionError](./unsupportedversionerror.md)
  Unsupported pass version.
- [PKPassKitError.Code.notEntitledError](./notentitlederror.md)
  Error caused by absence of the required entitlements for the given operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/invalidsignature)*