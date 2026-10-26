# audioMixInputParameters

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a mutable input parameters object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
+ (instancetype) audioMixInputParameters;
```

#### Return Value

A mutable input parameters object with no volume ramps and [`trackID`](./trackid.md) initialized to [`kCMPersistentTrackID_Invalid`](../../CoreMedia/kcmpersistenttrackid_invalid.md).

## See Also

### Creating input parameters
- [convenience init(track: AVAssetTrack?)](./init%28track%29.md)
  Creates a mutable input parameters object for a given track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/audiomixinputparameters)*