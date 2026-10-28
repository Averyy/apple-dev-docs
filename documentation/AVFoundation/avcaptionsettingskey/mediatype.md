# mediaType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

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

```c
extern AVCaptionSettingsKey const AVCaptionMediaTypeKey;
```

## Discussion

This includes the media types [`closedCaption`](../avmediatype/closedcaption.md) or [`subtitle`](../avmediatype/subtitle.md), for example.

## See Also

### Keys
- [static let mediaSubType: AVCaptionSettingsKey](./mediasubtype.md)
  A key that identifies the output media subtype of a caption conversion operation.
- [static let timeCodeFrameDuration: AVCaptionSettingsKey](./timecodeframeduration.md)
  A key that identifies the frame duration that the system uses for the time code.
- [static let useDropFrameTimeCode: AVCaptionSettingsKey](./usedropframetimecode.md)
  A key that identifies whether the system uses drop frame time code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionsettingskey/mediatype)*