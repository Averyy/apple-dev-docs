# warnings

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

This property value may change while the validator’s status is [`AVCaptionConversionValidator.Status.validating`](avcaptionconversionvalidator/status-swift.enum/validating.md).

## See Also

- [func validateCaptionConversion(warningHandler: (AVCaptionConversionWarning?) -> Void)](avcaptionconversionvalidator/validatecaptionconversion(warninghandler:).md)
  Validates the object’s captions.
- [class AVCaptionConversionWarning](avcaptionconversionwarning.md)
  An object that represents a conversion warning produced by a validator.
- [func stopValidating()](avcaptionconversionvalidator/stopvalidating.md)
  Stops the active validation operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/warnings)*