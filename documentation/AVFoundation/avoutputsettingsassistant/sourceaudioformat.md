# sourceAudioFormat

**Framework**: AVFoundation  
**Kind**: property

The format of the source audio data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sourceAudioFormat: CMAudioFormatDescription? { get set }
```

#### Discussion

The default value is `nil`, which means the assistant doesn’t know the audio format. Setting a value for this property helps the assistant generate more complete audio settings. After setting a value, requery the [`audioSettings`](avoutputsettingsassistant/audiosettings.md) property to get the latest values.

## See Also

- [var outputFileType: AVFileType](avoutputsettingsassistant/outputfiletype.md)
  A uniform type identifier (UTI) that indicates the type of file to write.
- [var audioSettings: [String : Any]?](avoutputsettingsassistant/audiosettings.md)
  An audio settings dictionary.
- [var videoSettings: [String : Any]?](avoutputsettingsassistant/videosettings.md)
  A video settings dictionary.
- [var sourceVideoFormat: CMVideoFormatDescription?](avoutputsettingsassistant/sourcevideoformat.md)
  The format of the source video data.
- [var sourceVideoMinFrameDuration: CMTime](avoutputsettingsassistant/sourcevideominframeduration.md)
  A time value that describes the minimum frame duration of the video data.
- [var sourceVideoAverageFrameDuration: CMTime](avoutputsettingsassistant/sourcevideoaverageframeduration.md)
  A time value that describes the average frame duration of the video data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/sourceaudioformat)*