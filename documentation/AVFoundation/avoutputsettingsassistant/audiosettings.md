# audioSettings

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An audio settings dictionary.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var audioSettings: [String : Any]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * audioSettings;
```

#### Discussion

The value of this property may change as a result of setting a new value for the [`sourceAudioFormat`](./sourceaudioformat.md) property. See [Audio settings](../audio-settings.md) for keys and values.

## See Also

### Configuring output settings
- [var outputFileType: AVFileType](./outputfiletype.md)
  A uniform type identifier (UTI) that indicates the type of file to write.
- [var sourceAudioFormat: CMAudioFormatDescription?](./sourceaudioformat.md)
  The format of the source audio data.
- [var videoSettings: [String : Any]?](./videosettings.md)
  A video settings dictionary.
- [var sourceVideoFormat: CMVideoFormatDescription?](./sourcevideoformat.md)
  The format of the source video data.
- [var sourceVideoMinFrameDuration: CMTime](./sourcevideominframeduration.md)
  A time value that describes the minimum frame duration of the video data.
- [var sourceVideoAverageFrameDuration: CMTime](./sourcevideoaverageframeduration.md)
  A time value that describes the average frame duration of the video data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant/audiosettings)*