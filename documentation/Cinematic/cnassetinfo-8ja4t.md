# CNAssetInfo

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object that provides Cinematic-specific information about an asset, including its tracks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNAssetInfo : NSObject
```

## Topics

### Instance Properties
- [allCinematicTracks](./cnassetinfo-8ja4t/allcinematictracks.md)
  An array of the Cinematic asset tracks.
- [asset](./cnassetinfo-8ja4t/asset.md)
  The original Cinematic source asset.
- [cinematicCapability](./cnassetinfo-8ja4t/cinematiccapability.md)
- [cinematicDisparityTrack](./cnassetinfo-8ja4t/cinematicdisparitytrack.md)
  The Cinematic disparity track.
- [cinematicMetadataTrack](./cnassetinfo-8ja4t/cinematicmetadatatrack.md)
  The Cinematic metadata track used.
- [cinematicVideoTrack](./cnassetinfo-8ja4t/cinematicvideotrack.md)
  Track used for Cinematic video.
- [frameTimingTrack](./cnassetinfo-8ja4t/frametimingtrack.md)
  The track used for Cinematic frame timing.
- [naturalSize](./cnassetinfo-8ja4t/naturalsize.md)
  The video size if rendered at its natural size.
- [preferredSize](./cnassetinfo-8ja4t/preferredsize.md)
  The video size if rendered at its natural size with the preferred transform applied.
- [preferredTransform](./cnassetinfo-8ja4t/preferredtransform.md)
  The preferred transform of the rendered image for display purposes.
- [preprocessed](./cnassetinfo-8ja4t/preprocessed.md)
  True only when an asset has been preprocessed
- [resourceStatus](./cnassetinfo-8ja4t/resourcestatus.md)
- [sampleDataTrackIDs](./cnassetinfo-8ja4t/sampledatatrackids.md)
  The source metadata track IDs required to implement the video composition instruction protocol.
- [timeRange](./cnassetinfo-8ja4t/timerange.md)
  The time range over which all Cinematic tracks are valid.
- [videoCompositionTrackIDs](./cnassetinfo-8ja4t/videocompositiontrackids.md)
  Source video track IDs required to implement the video composition instruction protocol.
- [videoCompositionTracks](./cnassetinfo-8ja4t/videocompositiontracks.md)
  Tracks required to construct the video composition output.
### Instance Methods
- [- downloadResourcesWithTimeout:completionHandler:](./cnassetinfo-8ja4t/downloadresourceswithtimeout_completionhandler_.md)
  Downloads the resources required to render cinematic effects for the given asset Resources are device-wide and are cached once downloaded
- [- preprocessAssetWithConfiguration:completionHandler:](./cnassetinfo-8ja4t/preprocessassetwithconfiguration_completionhandler_.md)
  Preprocesses the asset by generating a disparity track, writing the result to the URL specified in `configuration`. Required for assets whose `cinematicCapability` is \c CNCinematicCapabilityNeedsPreprocessing; on success \c assetInfo will be \c CNCinematicCapabilityRenderable.
### Type Properties
- [defaultResourceDownloadTimeout](./cnassetinfo-8ja4t/defaultresourcedownloadtimeout.md)
  Default timeout value for resource download for `+[CNAssetInfo downloadResourcesForVersions:timeout:completionHandler:]` `-[CNAssetInfo downloadResourcesWithTimeout:completionHandler:]`
### Type Methods
- [+ checkCinematicCapabilityForAsset:completionHandler:](./cnassetinfo-8ja4t/checkcinematiccapabilityforasset_completionhandler_.md)
  Asynchronously checks the cinematic capability of an asset. The completionHandler returns: CNCinematicCapabilityNone if a cinematic metadata track is not present. CNCinematicCapabilityRenderable if the cinematic asset can be used without preprocessing CNCinematicCapabilityNeedsPreprocessing If cinematic asset needs preprocessing before it can be used For assets that need preprocessing use [CNAssetInfo preprocessAssetWithConfiguration:completionHandler:] before using the asset
- [+ checkIfCinematic:completionHandler:](./cnassetinfo-8ja4t/checkifcinematic_completionhandler_.md)
  Determines if the asset is Cinematic.
- [+ downloadResourcesForVersions:timeout:completionHandler:](./cnassetinfo-8ja4t/downloadresourcesforversions_timeout_completionhandler_.md)
  Downloads the resources required to render cinematic effects on assets Resources are device-wide and are cached once downloaded
- [+ loadFromAsset:completionHandler:](./cnassetinfo-8ja4t/loadfromasset_completionhandler_.md)
  Loads the Cinematic asset information.
- [+ resourceStatusForVersions:](./cnassetinfo-8ja4t/resourcestatusforversions_.md)
  Check status for a set of resources.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CNCompositionInfo](./cncompositioninfo-vzoh.md)

## See Also

### Reading and rendering
- [CNCompositionInfo](./cncompositioninfo-vzoh.md)
  An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- [CNRenderingSession](./cnrenderingsession-8yghc.md)
  An object representing the context in which rendering occurs.
- [CNRenderingSessionAttributes](./cnrenderingsessionattributes.md)
  A structure for movie-wide attributes required for proper rendering.
- [CNRenderingSessionFrameAttributes](./cnrenderingsessionframeattributes.md)
  Creates an object with the per frame attributes that control the appearance of a single frame of the Cinematic movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-8ja4t)*