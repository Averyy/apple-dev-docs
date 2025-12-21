# AVCaptionConversionWarning

**Framework**: AVFoundation  
**Kind**: class

An object that represents a conversion warning produced by a validator.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionConversionWarning
```

## Topics

### Inspecting the warning
- [var warningType: AVCaptionConversionWarning.WarningType](avcaptionconversionwarning/warningtype-swift.property.md)
  A type that indicates the nature of the validation warning.
- [var rangeOfCaptions: NSRange](avcaptionconversionwarning/rangeofcaptions.md)
  The range of the captions for which the system issued a warning.
- [var adjustment: AVCaptionConversionAdjustment?](avcaptionconversionwarning/adjustment.md)
  A correction the converter makes when it converts a caption to a specific format.
- [class AVCaptionConversionAdjustment](avcaptionconversionadjustment.md)
  An object that describes an adjustment to correct a problem found during validation of a caption conversion.
- [AVCaptionConversionWarning.WarningType](avcaptionconversionwarning/warningtype-swift.struct.md)
  The type of a caption conversion warning.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func validateCaptionConversion(warningHandler: (AVCaptionConversionWarning?) -> Void)](avcaptionconversionvalidator/validatecaptionconversion(warninghandler:).md)
  Validates the object’s captions.
- [var warnings: [AVCaptionConversionWarning]](avcaptionconversionvalidator/warnings.md)
  The collection of warnings the validator encountered.
- [func stopValidating()](avcaptionconversionvalidator/stopvalidating.md)
  Stops the active validation operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning)*