# stopValidating()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) stopValidating;
```

## Discussion

You can call this method at any time, even within the validator’s callback to its handler.

Calling this method stops validation and changes the [`status`](./status-swift.property.md) value to [`AVCaptionConversionValidator.Status.stopped`](./status-swift.enum/stopped.md).

## See Also

### Validating captions
- [func validateCaptionConversion(warningHandler: (AVCaptionConversionWarning?) -> Void)](./validatecaptionconversion%28warninghandler%29.md)
  Validates the object’s captions.
- [var warnings: [AVCaptionConversionWarning]](./warnings.md)
  The collection of warnings the validator encountered.
- [class AVCaptionConversionWarning](../avcaptionconversionwarning.md)
  An object that represents a conversion warning produced by a validator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/stopvalidating())*