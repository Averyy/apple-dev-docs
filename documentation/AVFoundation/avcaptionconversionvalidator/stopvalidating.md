# stopValidating()

**Framework**: AVFoundation  
**Kind**: method

Stops the active validation operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func stopValidating()
```

#### Discussion

You can call this method at any time, even within the validator’s callback to its handler.

Calling this method stops validation and changes the [`status`](avcaptionconversionvalidator/status-swift.property.md) value to [`AVCaptionConversionValidator.Status.stopped`](avcaptionconversionvalidator/status-swift.enum/stopped.md).

## See Also

- [func validateCaptionConversion(warningHandler: (AVCaptionConversionWarning?) -> Void)](avcaptionconversionvalidator/validatecaptionconversion(warninghandler:).md)
  Validates the object’s captions.
- [var warnings: [AVCaptionConversionWarning]](avcaptionconversionvalidator/warnings.md)
  The collection of warnings the validator encountered.
- [class AVCaptionConversionWarning](avcaptionconversionwarning.md)
  An object that represents a conversion warning produced by a validator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/stopvalidating())*