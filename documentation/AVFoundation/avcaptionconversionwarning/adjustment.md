# adjustment

**Framework**: AVFoundation  
**Kind**: property

A correction the converter makes when it converts a caption to a specific format.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var adjustment: AVCaptionConversionAdjustment? { get }
```

#### Discussion

If this value is `nil` and you perform the conversion without correcting the problem, the system doesn’t include captions that you indicate in the output media data.

## See Also

- [var warningType: AVCaptionConversionWarning.WarningType](avcaptionconversionwarning/warningtype-swift.property.md)
  A type that indicates the nature of the validation warning.
- [var rangeOfCaptions: NSRange](avcaptionconversionwarning/rangeofcaptions.md)
  The range of the captions for which the system issued a warning.
- [class AVCaptionConversionAdjustment](avcaptionconversionadjustment.md)
  An object that describes an adjustment to correct a problem found during validation of a caption conversion.
- [AVCaptionConversionWarning.WarningType](avcaptionconversionwarning/warningtype-swift.struct.md)
  The type of a caption conversion warning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning/adjustment)*