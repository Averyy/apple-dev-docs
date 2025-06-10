# loadUneditedDuration(completionHandler:)

**Framework**: MediaExtension  
**Kind**: method

Returns the duration of the track, disregarding edits.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func uneditedDuration() async throws -> CMTime
```

#### Discussion

Media Toolbox uses this information to validate edit information and to check if the media is suitable for gapless playback.

## Parameters

- `completionHandler`: The completion block to execute when the load operation finishes.

## See Also

- [func loadTrackInfo(completionHandler: (METrackInfo?, (any Error)?) -> Void)](metrackreader/loadtrackinfo(completionhandler:).md)
  Loads the track info object with the properties of the media asset track.
- [func generateSampleCursor(atPresentationTimeStamp: CMTime, completionHandler: ((any MESampleCursor)?, (any Error)?) -> Void)](metrackreader/generatesamplecursor(atpresentationtimestamp:completionhandler:).md)
  Provides a new sample cursor that points to the sample at or near the specified presentation timestamp.
- [func generateSampleCursorAtFirstSampleInDecodeOrder(completionHandler: ((any MESampleCursor)?, (any Error)?) -> Void)](metrackreader/generatesamplecursoratfirstsampleindecodeorder(completionhandler:).md)
  Provides a new sample cursor that points to the first sample in decode order.
- [func generateSampleCursorAtLastSampleInDecodeOrder(completionHandler: ((any MESampleCursor)?, (any Error)?) -> Void)](metrackreader/generatesamplecursoratlastsampleindecodeorder(completionhandler:).md)
  Provides a new sample cursor that points to the last sample in decode order.
- [func loadTotalSampleDataLength(completionHandler: (Int64, (any Error)?) -> Void)](metrackreader/loadtotalsampledatalength(completionhandler:).md)
  Loads the total size in bytes of all the samples in the track.
- [func loadEstimatedDataRate(completionHandler: (Float32, (any Error)?) -> Void)](metrackreader/loadestimateddatarate(completionhandler:).md)
  Loads the approximate data rate of the track in bytes per second.
- [func loadMetadata(completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](metrackreader/loadmetadata(completionhandler:).md)
  Loads the array of metadata items from the media asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackreader/loaduneditedduration(completionhandler:))*