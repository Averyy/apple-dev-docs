# rangeOfCaptions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The range of the captions for which the system issued a warning.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var rangeOfCaptions: NSRange { get }
```

```objc
@property (readonly) NSRange rangeOfCaptions;
```

#### Discussion

This object only references captions with the same time range. If captions with different start times and durations have similar problems, or if individual captions have multiple problems, the validator generates separate instances of this class for each problem case.

## See Also

### Inspecting the warning
- [var warningType: AVCaptionConversionWarning.WarningType](./warningtype-swift.property.md)
  A type that indicates the nature of the validation warning.
- [var adjustment: AVCaptionConversionAdjustment?](./adjustment.md)
  A correction the converter makes when it converts a caption to a specific format.
- [class AVCaptionConversionAdjustment](../avcaptionconversionadjustment.md)
  An object that describes an adjustment to correct a problem found during validation of a caption conversion.
- [AVCaptionConversionWarning.WarningType](./warningtype-swift.struct.md)
  The type of a caption conversion warning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning/rangeofcaptions)*