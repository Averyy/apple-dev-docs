# CNAssetInfo

**Framework**: Cinematic  
**Kind**: class

An object that provides Cinematic-specific information about an asset, including its tracks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
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
- [var cinematicCapability: CNCinematicCapability](cnassetinfo-2ata2/cinematiccapability.md)
- [var cinematicDisparityTrack: AVAssetTrack](cnassetinfo-2ata2/cinematicdisparitytrack.md)
  The Cinematic disparity track.
- [var cinematicMetadataTrack: AVAssetTrack](cnassetinfo-2ata2/cinematicmetadatatrack.md)
  The Cinematic metadata track used.
- [var cinematicVideoTrack: AVAssetTrack](cnassetinfo-2ata2/cinematicvideotrack.md)
  Track used for Cinematic video.
- [var frameTimingTrack: AVAssetTrack](cnassetinfo-2ata2/frametimingtrack.md)
  The track used for Cinematic frame timing.
- [var isPreprocessed: Bool](cnassetinfo-2ata2/ispreprocessed.md)
- [var naturalSize: CGSize](cnassetinfo-2ata2/naturalsize.md)
  The video size if rendered at its natural size.
- [var preferredSize: CGSize](cnassetinfo-2ata2/preferredsize.md)
  The video size if rendered at its natural size with the preferred transform applied.
- [var preferredTransform: CGAffineTransform](cnassetinfo-2ata2/preferredtransform.md)
  The preferred transform of the rendered image for display purposes.
- [var resourceStatus: CNResourceStatus](cnassetinfo-2ata2/resourcestatus.md)
- [var sampleDataTrackIDs: [CMPersistentTrackID]](cnassetinfo-2ata2/sampledatatrackids.md)
  The source metadata track IDs required to implement the video composition instruction protocol.
- [var timeRange: CMTimeRange](cnassetinfo-2ata2/timerange.md)
  The time range over which all Cinematic tracks are valid.
- [var videoCompositionTrackIDs: [CMPersistentTrackID]](cnassetinfo-2ata2/videocompositiontrackids.md)
  Source video track IDs required to implement the video composition instruction protocol.
- [var videoCompositionTracks: [AVAssetTrack]](cnassetinfo-2ata2/videocompositiontracks.md)
  Tracks required to construct the video composition output.
### Instance Methods
- [func downloadResources(timeout: TimeInterval, subprogress: consuming Subprogress?) async throws -> CNAssetInfo](cnassetinfo-2ata2/downloadresources(timeout:subprogress:).md)
  Downloads the resources required to render cinematic effects for the given asset Resources are device-wide and are cached once downloaded
- [func preprocessAsset(configuration: CNAssetPreprocessConfiguration, subprogress: consuming Subprogress?) async throws -> CNAssetInfo](cnassetinfo-2ata2/preprocessasset(configuration:subprogress:).md)
  Preprocesses the asset by generating a disparity track, writing the result to the URL specified in `configuration`. Required for assets whose `cinematicCapability` is `.needsPreprocessing`; on success the returned `CNAssetInfo` will be `.renderable`.
### Type Properties
- [static var defaultResourceDownloadTimeout: TimeInterval](cnassetinfo-2ata2/defaultresourcedownloadtimeout.md)
  Default timeout value for resource download for: `public static func downloadResources(versions: Set<CNCinematicResourceVersion> = [], timeout: TimeInterval = defaultResourceDownloadTimeout, subprogress: consuming Subprogress? = nil) async throws` `public func downloadResources(timeout: TimeInterval = defaultResourceDownloadTimeout, subprogress: consuming Subprogress? = nil) async throws -> CNAssetInfo`
### Type Methods
- [class func cinematicCapability(for: AVAsset) async -> CNCinematicCapability](cnassetinfo-2ata2/cinematiccapability(for:).md)
  Asynchronously checks the cinematic capability of an asset. Returns CNCinematicCapability.none if a cinematic metadata track is not present. CNCinematicCapability.renderable if the cinematic asset can be used without preprocessing CNCinematicCapability.needsPreprocessing If cinematic asset needs preprocessing before it can be used For assets that need preprocessing use `CNAssetInfo.preprocessAsset(configuration:subprogress:)` before using the asset
- [static func downloadResources(versions: Set<CNCinematicResourceVersion>, timeout: TimeInterval, subprogress: consuming Subprogress?) async throws](cnassetinfo-2ata2/downloadresources(versions:timeout:subprogress:).md)
  Downloads the resources required to render cinematic effects on assets Resources are device-wide and are cached once downloaded
- [class func isCinematic(asset: AVAsset) async -> Bool](cnassetinfo-2ata2/iscinematic(asset:).md)
  Determines if the asset is Cinematic asynchronously.
- [static func resourceStatus(for: Set<CNCinematicResourceVersion>) -> CNResourceStatus](cnassetinfo-2ata2/resourcestatus(for:).md)
  Check status for a set of resources.

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