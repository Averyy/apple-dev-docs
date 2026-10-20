# warningType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A type that indicates the nature of the validation warning.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var warningType: AVCaptionConversionWarning.WarningType { get }
```

```objc
@property (readonly) AVCaptionConversionWarningType warningType;
```

## See Also

### Inspecting the warning
- [var rangeOfCaptions: NSRange](./rangeofcaptions.md)
  The range of the captions for which the system issued a warning.
- [var adjustment: AVCaptionConversionAdjustment?](./adjustment.md)
  A correction the converter makes when it converts a caption to a specific format.
- [class AVCaptionConversionAdjustment](../avcaptionconversionadjustment.md)
  An object that describes an adjustment to correct a problem found during validation of a caption conversion.
- [AVCaptionConversionWarning.WarningType](./warningtype-swift.struct.md)
  The type of a caption conversion warning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning/warningtype-swift.property)*