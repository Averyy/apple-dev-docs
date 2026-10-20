# init(assetTrack:)

**Framework**: AVFoundation  
**Kind**: init

Creates a new mutable video composition layer instruction for the given track.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(assetTrack track: AVAssetTrack)
```

#### Return Value

A new mutable video composition layer instruction with no transform or opacity ramps and [`trackID`](avmutablevideocompositionlayerinstruction/trackid.md) initialized to the track ID of `track`.

## Parameters

- `track`: The asset track to which to apply the instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocompositionlayerinstruction/init(assettrack:))*