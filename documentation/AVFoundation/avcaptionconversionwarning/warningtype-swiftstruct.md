# AVCaptionConversionWarning.WarningType

**Framework**: AVFoundation  
**Kind**: struct

The type of a caption conversion warning.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct WarningType
```

## Topics

### Warning Types
- [static let excessMediaData: AVCaptionConversionWarning.WarningType](avcaptionconversionwarning/warningtype-swift.struct/excessmediadata.md)
  A type that indicates one or more captions exceed the media data capacity for media of the type and subtype that the conversion settings specify.
### Initializers
- [init(rawValue: String)](avcaptionconversionwarning/warningtype-swift.struct/init(rawvalue:).md)
  Creates a warning type with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var warningType: AVCaptionConversionWarning.WarningType](avcaptionconversionwarning/warningtype-swift.property.md)
  A type that indicates the nature of the validation warning.
- [var rangeOfCaptions: NSRange](avcaptionconversionwarning/rangeofcaptions.md)
  The range of the captions for which the system issued a warning.
- [var adjustment: AVCaptionConversionAdjustment?](avcaptionconversionwarning/adjustment.md)
  A correction the converter makes when it converts a caption to a specific format.
- [class AVCaptionConversionAdjustment](avcaptionconversionadjustment.md)
  An object that describes an adjustment to correct a problem found during validation of a caption conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionwarning/warningtype-swift.struct)*