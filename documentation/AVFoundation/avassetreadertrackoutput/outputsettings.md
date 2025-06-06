# outputSettings

**Framework**: AVFoundation  
**Kind**: property

The output settings for this track output.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var outputSettings: [String : Any]? { get }
```

#### Discussion

The value is a dictionary that contains values for audio and video settings keys. A value of `nil` indicates that the track output vends samples in their original format as stored in the target track.

## See Also

- [var track: AVAssetTrack](avassetreadertrackoutput/track.md)
  The track from which the output reads sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadertrackoutput/outputsettings)*