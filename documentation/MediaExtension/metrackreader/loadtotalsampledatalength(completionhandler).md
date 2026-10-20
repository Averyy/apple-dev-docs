# loadTotalSampleDataLength(completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Loads the total size in bytes of all the samples in the track.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func loadTotalSampleDataLength(completionHandler: @escaping @Sendable (Int64, (any Error)?) -> Void)
```

```swift
optional func totalSampleDataLength() async throws -> Int64
```

```objc
- (void) loadTotalSampleDataLengthWithCompletionHandler:(void (^)(int64_t totalSampleDataLength, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: The completion block to execute when the load operation finishes.

## See Also

### Getting track information
- [func loadTrackInfo(completionHandler: (METrackInfo?, (any Error)?) -> Void)](./loadtrackinfo%28completionhandler%29.md)
  Loads the track info object with the properties of the media asset track.
- [func generateSampleCursor(atPresentationTimeStamp: CMTime, completionHandler: ((any MESampleCursor)?, (any Error)?) -> Void)](./generatesamplecursor%28atpresentationtimestamp,completionhandler%29.md)
  Provides a new sample cursor that points to the sample at or near the specified presentation timestamp.
- [func generateSampleCursorAtFirstSampleInDecodeOrder(completionHandler: ((any MESampleCursor)?, (any Error)?) -> Void)](./generatesamplecursoratfirstsampleindecodeorder%28completionhandler%29.md)
  Provides a new sample cursor that points to the first sample in decode order.
- [func generateSampleCursorAtLastSampleInDecodeOrder(completionHandler: ((any MESampleCursor)?, (any Error)?) -> Void)](./generatesamplecursoratlastsampleindecodeorder%28completionhandler%29.md)
  Provides a new sample cursor that points to the last sample in decode order.
- [func loadUneditedDuration(completionHandler: (CMTime, (any Error)?) -> Void)](./loaduneditedduration%28completionhandler%29.md)
  Returns the duration of the track, disregarding edits.
- [func loadEstimatedDataRate(completionHandler: (Float32, (any Error)?) -> Void)](./loadestimateddatarate%28completionhandler%29.md)
  Loads the approximate data rate of the track in bytes per second.
- [func loadMetadata(completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](./loadmetadata%28completionhandler%29.md)
  Loads the array of metadata items from the media asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/metrackreader/loadtotalsampledatalength(completionhandler:))*