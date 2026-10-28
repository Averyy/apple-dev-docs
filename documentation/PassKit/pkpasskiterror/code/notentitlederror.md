# PKPassKitError.Code.notEntitledError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

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

```c
PKNotEntitledError
```

## Discussion

Apps require appropriate entitlements to read, update or delete passes. To add these entitlements, enable the Wallet capabilities in Xcode.

## See Also

### Error codes
- [PKPassKitError.Code.unknownError](./unknownerror.md)
  Unknown error.
- [PKPassKitError.Code.invalidDataError](./invaliddataerror.md)
  Invalid pass data.
- [PKPassKitError.Code.unsupportedVersionError](./unsupportedversionerror.md)
  Unsupported pass version.
- [PKPassKitError.Code.invalidSignature](./invalidsignature.md)
  Invalid pass signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasskiterror/code/notentitlederror)*