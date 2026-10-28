# videoCompositionLayerInstruction

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new mutable video composition layer instruction.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) videoCompositionLayerInstruction;
```

## Return Value

A new mutable video composition layer instruction with no transform or opacity ramps and [`trackID`](./trackid.md) initialized to [`kCMPersistentTrackID_Invalid`](../../CoreMedia/kcmpersistenttrackid_invalid.md).

## See Also

### Creating an instruction
- [convenience init(assetTrack: AVAssetTrack)](./init%28assettrack%29.md)
  Creates a new mutable video composition layer instruction for the given track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/videocompositionlayerinstruction)*