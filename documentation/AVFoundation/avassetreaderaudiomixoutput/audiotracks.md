# audioTracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The tracks from which the output reads audio.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var audioTracks: [AVAssetTrack] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVAssetTrack *> * audioTracks;
```

## See Also

### Inspecting an output
- [var audioSettings: [String : Any]?](./audiosettings.md)
  The audio settings that the output uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput/audiotracks)*