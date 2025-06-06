# CNAssetInfo

**Framework**: Cinematic  
**Kind**: class

An object that provides Cinematic-specific information about an asset, including its tracks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class CNAssetInfo
```

## Topics

### Initializers
- [init(asset: AVAsset) async throws](cnassetinfo-2ata2/init(asset:).md)
  Creates a Cinematic object from an asset.
### Instance Properties
- [var allCinematicTracks: [AVAssetTrack]](cnassetinfo-2ata2/allcinematictracks.md)
  An array of the Cinematic asset tracks.
- [let asset: AVAsset](cnassetinfo-2ata2/asset.md)
  The original Cinematic source asset.
- [var cinematicDisparityTrack: AVAssetTrack](cnassetinfo-2ata2/cinematicdisparitytrack.md)
  The Cinematic disparity track.
- [var cinematicMetadataTrack: AVAssetTrack](cnassetinfo-2ata2/cinematicmetadatatrack.md)
  The Cinematic metadata track used.
- [var cinematicVideoTrack: AVAssetTrack](cnassetinfo-2ata2/cinematicvideotrack.md)
  Track used for Cinematic video.
- [var frameTimingTrack: AVAssetTrack](cnassetinfo-2ata2/frametimingtrack.md)
  The track used for Cinematic frame timing.
- [var naturalSize: CGSize](cnassetinfo-2ata2/naturalsize.md)
  The video size if rendered at its natural size.
- [var preferredSize: CGSize](cnassetinfo-2ata2/preferredsize.md)
  The video size if rendered at its natural size with the preferred transform applied.
- [var preferredTransform: CGAffineTransform](cnassetinfo-2ata2/preferredtransform.md)
  The preferred transform of the rendered image for display purposes.
- [var sampleDataTrackIDs: [CMPersistentTrackID]](cnassetinfo-2ata2/sampledatatrackids.md)
  The source metadata track IDs required to implement the video composition instruction protocol.
- [var timeRange: CMTimeRange](cnassetinfo-2ata2/timerange.md)
  The time range over which all Cinematic tracks are valid.
- [var videoCompositionTrackIDs: [CMPersistentTrackID]](cnassetinfo-2ata2/videocompositiontrackids.md)
  Source video track IDs required to implement the video composition instruction protocol.
- [var videoCompositionTracks: [AVAssetTrack]](cnassetinfo-2ata2/videocompositiontracks.md)
  Tracks required to construct the video composition output.
### Type Methods
- [class func isCinematic(asset: AVAsset) async -> Bool](cnassetinfo-2ata2/iscinematic(asset:).md)
  Determines if the asset is Cinematic asynchronously.

## Relationships

### Inherited By
- [CNCompositionInfo](cncompositioninfo-7eunn.md)

## See Also

- [class CNCompositionInfo](cncompositioninfo-7eunn.md)
  An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- [class CNRenderingSession](cnrenderingsession-1hzh8.md)
  An object representing the context in which rendering occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-2ata2)*