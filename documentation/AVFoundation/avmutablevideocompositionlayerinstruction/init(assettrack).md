# init(assetTrack:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a new mutable video composition layer instruction for the given track.

**Availability**:
- iOS 4.0+ - Deprecated in 26.0
- iPadOS 4.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.7+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use AVVideoCompositionLayerInstruction.Configuration instead

## Declaration

```swift
convenience init(assetTrack track: AVAssetTrack)
```

```objc
+ (instancetype) videoCompositionLayerInstructionWithAssetTrack:(AVAssetTrack *) track;
```

## Return Value

A new mutable video composition layer instruction with no transform or opacity ramps and [`trackID`](./trackid.md) initialized to the track ID of `track`.

## Parameters

- `track`: The asset track to which to apply the instruction.

## See Also

### Creating an instruction
- [+ videoCompositionLayerInstruction](./videocompositionlayerinstruction.md)
  Returns a new mutable video composition layer instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/init(assettrack:))*