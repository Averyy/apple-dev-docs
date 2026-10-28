# sourceVideoFormat

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The format of the source video data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sourceVideoFormat: CMVideoFormatDescription? { get set }
```

```objc
@property (nonatomic, retain, nullable) CMVideoFormatDescriptionRef sourceVideoFormat;
```

## Discussion

The default value is `nil`, which means the assistant doesn’t know the video format. Setting a value for this property helps the assistant generate more complete video settings. After setting a value, requery the [`videoSettings`](./videosettings.md) property to get the latest values.

## See Also

### Configuring output settings
- [var outputFileType: AVFileType](./outputfiletype.md)
  A uniform type identifier (UTI) that indicates the type of file to write.
- [var audioSettings: [String : Any]?](./audiosettings.md)
  An audio settings dictionary.
- [var sourceAudioFormat: CMAudioFormatDescription?](./sourceaudioformat.md)
  The format of the source audio data.
- [var videoSettings: [String : Any]?](./videosettings.md)
  A video settings dictionary.
- [var sourceVideoMinFrameDuration: CMTime](./sourcevideominframeduration.md)
  A time value that describes the minimum frame duration of the video data.
- [var sourceVideoAverageFrameDuration: CMTime](./sourcevideoaverageframeduration.md)
  A time value that describes the average frame duration of the video data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/sourcevideoformat)*