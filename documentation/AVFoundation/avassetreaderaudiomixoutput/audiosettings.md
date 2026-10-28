# audioSettings

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The audio settings that the output uses.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var audioSettings: [String : Any]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * audioSettings;
```

## Discussion

The dictionary must contain values for the keys in [Linear PCM format settings](../linear-pcm-format-settings.md).

Setting the property value to `nil` indicates that the output returns audio samples in an uncompressed format.

## See Also

### Inspecting an output
- [var audioTracks: [AVAssetTrack]](./audiotracks.md)
  The tracks from which the output reads audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/audiosettings)*