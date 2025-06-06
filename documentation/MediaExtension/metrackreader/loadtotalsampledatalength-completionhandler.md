# loadTotalSampleDataLength(completionHandler:)

**Framework**: MediaExtension  
**Kind**: method

Loads the total size in bytes of all the samples in the track.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var totalSampleDataLength: Int64 { get async throws }
```

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
- [func loadUneditedDuration(completionHandler: (CMTime, (any Error)?) -> Void)](metrackreader/loaduneditedduration(completionhandler:).md)
  Returns the duration of the track, disregarding edits.
- [func loadEstimatedDataRate(completionHandler: (Float32, (any Error)?) -> Void)](metrackreader/loadestimateddatarate(completionhandler:).md)
  Loads the approximate data rate of the track in bytes per second.
- [func loadMetadata(completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](metrackreader/loadmetadata(completionhandler:).md)
  Loads the array of metadata items from the media asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackreader/loadtotalsampledatalength(completionhandler:))*