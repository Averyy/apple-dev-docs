# timeCodeFrameDuration

**Framework**: AVFoundation  
**Kind**: property

A key that identifies the frame duration that the system uses for the time code.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
static let timeCodeFrameDuration: AVCaptionSettingsKey
```

#### Discussion

Some formats, such as TTML, use time code notation to indicate the timing of a caption. Use this key to specify the frame rate of the time code.

## See Also

- [static let mediaType: AVCaptionSettingsKey](avcaptionsettingskey/mediatype.md)
  A key that identifies the output media type of a caption conversion operation.
- [static let mediaSubType: AVCaptionSettingsKey](avcaptionsettingskey/mediasubtype.md)
  A key that identifies the output media subtype of a caption conversion operation.
- [static let useDropFrameTimeCode: AVCaptionSettingsKey](avcaptionsettingskey/usedropframetimecode.md)
  A key that identifies whether the system uses drop frame time code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionsettingskey/timecodeframeduration)*