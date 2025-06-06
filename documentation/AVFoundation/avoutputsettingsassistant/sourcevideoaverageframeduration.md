# sourceVideoAverageFrameDuration

**Framework**: AVFoundation  
**Kind**: property

A time value that describes the average frame duration of the video data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sourceVideoAverageFrameDuration: CMTime { get set }
```

#### Discussion

Setting this property enables the output settings assistant to generate more complete video settings. After setting a value, requery the [`videoSettings`](avoutputsettingsassistant/videosettings.md) property to get the latest values.

The default value is `1/30`, which means the output settings assistant assumes that your source video has a frame rate of 30fps.

## See Also

- [var outputFileType: AVFileType](avoutputsettingsassistant/outputfiletype.md)
  A uniform type identifier (UTI) that indicates the type of file to write.
- [var audioSettings: [String : Any]?](avoutputsettingsassistant/audiosettings.md)
  An audio settings dictionary.
- [var sourceAudioFormat: CMAudioFormatDescription?](avoutputsettingsassistant/sourceaudioformat.md)
  The format of the source audio data.
- [var videoSettings: [String : Any]?](avoutputsettingsassistant/videosettings.md)
  A video settings dictionary.
- [var sourceVideoFormat: CMVideoFormatDescription?](avoutputsettingsassistant/sourcevideoformat.md)
  The format of the source video data.
- [var sourceVideoMinFrameDuration: CMTime](avoutputsettingsassistant/sourcevideominframeduration.md)
  A time value that describes the minimum frame duration of the video data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/sourcevideoaverageframeduration)*