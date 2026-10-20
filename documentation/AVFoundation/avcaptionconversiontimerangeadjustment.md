# AVCaptionConversionTimeRangeAdjustment

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that describes an adjustment to the time range of one or more captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionConversionTimeRangeAdjustment
```

```objc
@interface AVCaptionConversionTimeRangeAdjustment : AVCaptionConversionAdjustment
```

## Topics

### Accessing time offsets
- [var startTimeOffset: CMTime](./avcaptionconversiontimerangeadjustment/starttimeoffset.md)
  The time value by which the system offsets the start times of captions to correct a problem.
- [var durationOffset: CMTime](./avcaptionconversiontimerangeadjustment/durationoffset.md)
  The time value by which the system offsets the durations of captions to correct a problem.

## Relationships

### Inherits From
- [AVCaptionConversionAdjustment](./avcaptionconversionadjustment.md)
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

### Accessing the adjustment type
- [var adjustmentType: AVCaptionConversionAdjustment.AdjustmentType](./avcaptionconversionadjustment/adjustmenttype-swift.property.md)
  The type of caption conversion adjustment.
- [AVCaptionConversionAdjustment.AdjustmentType](./avcaptionconversionadjustment/adjustmenttype-swift.struct.md)
  Constants that indicate an adjustment type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversiontimerangeadjustment)*