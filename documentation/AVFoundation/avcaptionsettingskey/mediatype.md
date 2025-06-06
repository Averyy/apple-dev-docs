# mediaType

**Framework**: AVFoundation  
**Kind**: property

A key that identifies the output media type of a caption conversion operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
static let mediaType: AVCaptionSettingsKey
```

#### Discussion

This includes the media types [`closedCaption`](avmediatype/closedcaption.md) or [`subtitle`](avmediatype/subtitle.md), for example.

## See Also

- [static let mediaSubType: AVCaptionSettingsKey](avcaptionsettingskey/mediasubtype.md)
  A key that identifies the output media subtype of a caption conversion operation.
- [static let timeCodeFrameDuration: AVCaptionSettingsKey](avcaptionsettingskey/timecodeframeduration.md)
  A key that identifies the frame duration that the system uses for the time code.
- [static let useDropFrameTimeCode: AVCaptionSettingsKey](avcaptionsettingskey/usedropframetimecode.md)
  A key that identifies whether the system uses drop frame time code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionsettingskey/mediatype)*