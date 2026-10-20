# videoSettings

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The video settings that the output uses.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var videoSettings: [String : Any]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * videoSettings;
```

## See Also

### Inspecting an output
- [var videoTracks: [AVAssetTrack]](./videotracks.md)
  The tracks from which the output reads the composited video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/videosettings)*