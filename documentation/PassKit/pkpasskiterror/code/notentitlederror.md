# PKPassKitError.Code.notEntitledError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

Error caused by absence of the required entitlements for the given operation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case notEntitledError
```

#### Discussion

Apps require appropriate entitlements to read, update or delete passes. To add these entitlements, enable the Wallet capabilities in Xcode.

## See Also

- [PKPassKitError.Code.unknownError](pkpasskiterror/code/unknownerror.md)
  Unknown error.
- [PKPassKitError.Code.invalidDataError](pkpasskiterror/code/invaliddataerror.md)
  Invalid pass data.
- [PKPassKitError.Code.unsupportedVersionError](pkpasskiterror/code/unsupportedversionerror.md)
  Unsupported pass version.
- [PKPassKitError.Code.invalidSignature](pkpasskiterror/code/invalidsignature.md)
  Invalid pass signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/notentitlederror)*