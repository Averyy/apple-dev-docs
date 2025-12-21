# useDropFrameTimeCode

**Framework**: AVFoundation  
**Kind**: property

A key that identifies whether the system uses drop frame time code.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
static let useDropFrameTimeCode: AVCaptionSettingsKey
```

#### Discussion

Some formats, such as SCC, use time code notation to indicate the timing of a caption. Use the property to specify whether the system uses the drop frame time code or non-drop frame time code.

The default is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [static let mediaType: AVCaptionSettingsKey](avcaptionsettingskey/mediatype.md)
  A key that identifies the output media type of a caption conversion operation.
- [static let mediaSubType: AVCaptionSettingsKey](avcaptionsettingskey/mediasubtype.md)
  A key that identifies the output media subtype of a caption conversion operation.
- [static let timeCodeFrameDuration: AVCaptionSettingsKey](avcaptionsettingskey/timecodeframeduration.md)
  A key that identifies the frame duration that the system uses for the time code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionsettingskey/usedropframetimecode)*