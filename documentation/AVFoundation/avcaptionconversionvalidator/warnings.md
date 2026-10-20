# warnings

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The collection of warnings the validator encountered.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var warnings: [AVCaptionConversionWarning] { get }
```

```objc
@property (readonly) NSArray<AVCaptionConversionWarning *> * warnings;
```

#### Discussion

This property value may change while the validator’s status is [`AVCaptionConversionValidator.Status.validating`](./status-swift.enum/validating.md).

## See Also

### Validating captions
- [func validateCaptionConversion(warningHandler: (AVCaptionConversionWarning?) -> Void)](./validatecaptionconversion%28warninghandler%29.md)
  Validates the object’s captions.
- [class AVCaptionConversionWarning](../avcaptionconversionwarning.md)
  An object that represents a conversion warning produced by a validator.
- [func stopValidating()](./stopvalidating%28%29.md)
  Stops the active validation operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/warnings)*