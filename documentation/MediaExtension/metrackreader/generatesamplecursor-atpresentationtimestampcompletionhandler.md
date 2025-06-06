# generateSampleCursor(atPresentationTimeStamp:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Required**: Yes

Provides a new sample cursor that points to the sample at or near the specified presentation timestamp.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func sampleCursor(atPresentationTimeStamp presentationTimeStamp: CMTime) async throws -> any MESampleCursor
```

#### Discussion

The new sample cursor points to the last sample with a presentation time stamp (PTS) less than or equal to `presentationTimeStamp`, or if there are no such samples, the first sample in PTS order.

## Parameters

- `presentationTimeStamp`: The presentation time stamp.
- `completionHandler`: The completion block to execute when the generate operation finishes.

## See Also

- [func loadTrackInfo(completionHandler: (METrackInfo?, (any Error)?) -> Void)](metrackreader/loadtrackinfo(completionhandler:).md)
  Loads the track info object with the properties of the media asset track.
- [func generateSampleCursorAtFirstSampleInDecodeOrder(completionHandler: ((any MESampleCursor)?, (any Error)?) -> Void)](metrackreader/generatesamplecursoratfirstsampleindecodeorder(completionhandler:).md)
  Provides a new sample cursor that points to the first sample in decode order.
- [func generateSampleCursorAtLastSampleInDecodeOrder(completionHandler: ((any MESampleCursor)?, (any Error)?) -> Void)](metrackreader/generatesamplecursoratlastsampleindecodeorder(completionhandler:).md)
  Provides a new sample cursor that points to the last sample in decode order.
- [func loadUneditedDuration(completionHandler: (CMTime, (any Error)?) -> Void)](metrackreader/loaduneditedduration(completionhandler:).md)
  Returns the duration of the track, disregarding edits.
- [func loadTotalSampleDataLength(completionHandler: (Int64, (any Error)?) -> Void)](metrackreader/loadtotalsampledatalength(completionhandler:).md)
  Loads the total size in bytes of all the samples in the track.
- [func loadEstimatedDataRate(completionHandler: (Float32, (any Error)?) -> Void)](metrackreader/loadestimateddatarate(completionhandler:).md)
  Loads the approximate data rate of the track in bytes per second.
- [func loadMetadata(completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](metrackreader/loadmetadata(completionhandler:).md)
  Loads the array of metadata items from the media asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackreader/generatesamplecursor(atpresentationtimestamp:completionhandler:))*