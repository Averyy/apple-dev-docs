# videoSettings

**Framework**: AVFoundation  
**Kind**: property

A video settings dictionary.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var videoSettings: [String : Any]? { get }
```

#### Discussion

The value of this property may change as a result of setting a new value for the [`sourceVideoFormat`](avoutputsettingsassistant/sourcevideoformat.md) property. See [`Video settings`](video-settings.md) for the supported keys and values.

## See Also

- [var outputFileType: AVFileType](avoutputsettingsassistant/outputfiletype.md)
  A uniform type identifier (UTI) that indicates the type of file to write.
- [var audioSettings: [String : Any]?](avoutputsettingsassistant/audiosettings.md)
  An audio settings dictionary.
- [var sourceAudioFormat: CMAudioFormatDescription?](avoutputsettingsassistant/sourceaudioformat.md)
  The format of the source audio data.
- [var sourceVideoFormat: CMVideoFormatDescription?](avoutputsettingsassistant/sourcevideoformat.md)
  The format of the source video data.
- [var sourceVideoMinFrameDuration: CMTime](avoutputsettingsassistant/sourcevideominframeduration.md)
  A time value that describes the minimum frame duration of the video data.
- [var sourceVideoAverageFrameDuration: CMTime](avoutputsettingsassistant/sourcevideoaverageframeduration.md)
  A time value that describes the average frame duration of the video data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/videosettings)*