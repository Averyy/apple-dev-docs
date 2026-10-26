# preserveAlternateTracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A policy that passes through alternate audio tracks from the source asset during export.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var preserveAlternateTracks: AVAssetTrackGroupOutputHandling { get }
```

```c
AVAssetTrackGroupOutputHandlingPreserveAlternateTracks
```

#### Discussion

Setting this policy tells the session to export alternate tracks in a track group without reencoding them.

## See Also

### Policies
- [AVAssetTrackGroupOutputHandlingNone](./avassettrackgroupoutputhandlingnone.md)
  A policy that doesn’t pass through alternate audio tracks from the source asset during export.
- [AVAssetTrackGroupOutputHandlingDefaultPolicy](./avassettrackgroupoutputhandlingdefaultpolicy.md)
  The default track group output handling policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackgroupoutputhandling/preservealternatetracks)*