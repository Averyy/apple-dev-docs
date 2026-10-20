# AVCaptionConversionAdjustment

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptionConversionAdjustment : NSObject
```

## Topics

### Accessing the adjustment type
- [var adjustmentType: AVCaptionConversionAdjustment.AdjustmentType](./avcaptionconversionadjustment/adjustmenttype-swift.property.md)
  The type of caption conversion adjustment.
- [AVCaptionConversionAdjustment.AdjustmentType](./avcaptionconversionadjustment/adjustmenttype-swift.struct.md)
  Constants that indicate an adjustment type.
- [class AVCaptionConversionTimeRangeAdjustment](./avcaptionconversiontimerangeadjustment.md)
  An object that describes an adjustment to the time range of one or more captions.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVCaptionConversionTimeRangeAdjustment](./avcaptionconversiontimerangeadjustment.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Inspecting the warning
- [var warningType: AVCaptionConversionWarning.WarningType](./avcaptionconversionwarning/warningtype-swift.property.md)
  A type that indicates the nature of the validation warning.
- [var rangeOfCaptions: NSRange](./avcaptionconversionwarning/rangeofcaptions.md)
  The range of the captions for which the system issued a warning.
- [var adjustment: AVCaptionConversionAdjustment?](./avcaptionconversionwarning/adjustment.md)
  A correction the converter makes when it converts a caption to a specific format.
- [AVCaptionConversionWarning.WarningType](./avcaptionconversionwarning/warningtype-swift.struct.md)
  The type of a caption conversion warning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionadjustment)*