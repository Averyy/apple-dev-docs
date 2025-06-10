# AVCaptionSettingsKey

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines dictionary keys to configure the caption converter and validator.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct AVCaptionSettingsKey
```

## Topics

### Keys
- [static let mediaType: AVCaptionSettingsKey](avcaptionsettingskey/mediatype.md)
  A key that identifies the output media type of a caption conversion operation.
- [static let mediaSubType: AVCaptionSettingsKey](avcaptionsettingskey/mediasubtype.md)
  A key that identifies the output media subtype of a caption conversion operation.
- [static let timeCodeFrameDuration: AVCaptionSettingsKey](avcaptionsettingskey/timecodeframeduration.md)
  A key that identifies the frame duration that the system uses for the time code.
- [static let useDropFrameTimeCode: AVCaptionSettingsKey](avcaptionsettingskey/usedropframetimecode.md)
  A key that identifies whether the system uses drop frame time code.
### Initializers
- [init(rawValue: String)](avcaptionsettingskey/init(rawvalue:).md)
  Creates a settings key with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVCaptionFormatConformer](avcaptionformatconformer.md)
  An object that converts a canonical caption to a specific format.
- [class AVCaptionConversionValidator](avcaptionconversionvalidator.md)
  An object that validates captions for a conversion operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionsettingskey)*