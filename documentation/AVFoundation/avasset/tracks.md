# tracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The tracks an asset contains.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`tracks`](../avpartialasyncproperty/tracks-48zyw.md) asynchronously instead.

## Declaration

```swift
var tracks: [AVAssetTrack] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVAssetTrack *> * tracks;
```

## See Also

### Accessing tracks
- [- trackWithTrackID:](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [- tracksWithMediaType:](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [- tracksWithMediaCharacteristic:](./tracks%28withmediacharacteristic%29.md)
  Returns an array of asset tracks matching the specified media characteristic.
- [- unusedTrackID](./unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/tracks)*