# sampleLocation()

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Returns the location and byte source of the sample indicated by the cursor.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func sampleLocation() throws -> MESampleLocation
```

```objc
- (MESampleLocation *) sampleLocationReturningError:(NSError **) error;
```

## Return Value

A sample location.

## Discussion

Sample data needs to be contiguous. If the sample data isn’t contiguous or the cursor doesn’t support this method, it fails with the error [`MEError.Code.locationNotAvailable`](../meerror-swift.struct/code/locationnotavailable.md). In this case, use [`loadSampleBufferContainingSamples(to:completionHandler:)`](./loadsamplebuffercontainingsamples%28to,completionhandler%29.md) to load the data.

If it’s not possible to implement this method, implement [`estimatedSampleLocation()`](./estimatedsamplelocation%28%29.md) to get an estimated sample location, and [`refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)`](./refinesamplelocation%28_,refinementdata,refinementdatalength,refinedlocation%29.md) to analyze this data and provide precise location and size info.

## See Also

### Sending samples to a pipeline
- [func chunkDetails() throws -> MESampleCursorChunk](./chunkdetails%28%29.md)
  Returns information about the chunk that holds the sample indicated by the cursor.
- [func loadSampleBufferContainingSamples(to: (any MESampleCursor)?, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](./loadsamplebuffercontainingsamples%28to,completionhandler%29.md)
  Builds a sample buffer that contains the samples at the cursor that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/samplelocation())*