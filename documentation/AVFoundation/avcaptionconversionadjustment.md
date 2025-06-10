# AVCaptionConversionAdjustment

**Framework**: AVFoundation  
**Kind**: class

An object that describes an adjustment to correct a problem found during validation of a caption conversion.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionConversionAdjustment
```

## Topics

### Accessing the Adjustment Type
- [var adjustmentType: AVCaptionConversionAdjustment.AdjustmentType](avcaptionconversionadjustment/adjustmenttype-swift.property.md)
  The type of caption conversion adjustment.
- [AVCaptionConversionAdjustment.AdjustmentType](avcaptionconversionadjustment/adjustmenttype-swift.struct.md)
  Constants that indicate an adjustment type.
- [class AVCaptionConversionTimeRangeAdjustment](avcaptionconversiontimerangeadjustment.md)
  An object that describes an adjustment to the time range of one or more captions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVCaptionConversionTimeRangeAdjustment](avcaptionconversiontimerangeadjustment.md)
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

- [var warningType: AVCaptionConversionWarning.WarningType](avcaptionconversionwarning/warningtype-swift.property.md)
  A type that indicates the nature of the validation warning.
- [var rangeOfCaptions: NSRange](avcaptionconversionwarning/rangeofcaptions.md)
  The range of the captions for which the system issued a warning.
- [var adjustment: AVCaptionConversionAdjustment?](avcaptionconversionwarning/adjustment.md)
  A correction the converter makes when it converts a caption to a specific format.
- [AVCaptionConversionWarning.WarningType](avcaptionconversionwarning/warningtype-swift.struct.md)
  The type of a caption conversion warning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionadjustment)*