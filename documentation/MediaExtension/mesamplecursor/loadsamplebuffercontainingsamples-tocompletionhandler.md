# loadSampleBufferContainingSamples(to:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method

Builds a sample buffer that contains the samples at the cursor that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func loadSampleBufferContainingSamples(to endSampleCursor: (any MESampleCursor)?) async throws -> CMSampleBuffer
```

#### Discussion

Plugin format readers that don’t implement [`sampleLocation()`](mesamplecursor/samplelocation().md) or that always load sample data to answer cursor queries need to implement this method. If a plug-in format reader implements [`sampleLocation()`](mesamplecursor/samplelocation().md), implementing [`loadSampleBufferContainingSamples(to:completionHandler:)`](mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:).md) is optional.

If there’s no sample data between the sample cursor and `endSampleCursor`, the sample buffer is empty. If an error occurs, the sample buffer is `nil`.

> ❗ **Important**:  If there’s a change of format description between the sample cursor and `endSampleCursor`, the returned sample buffer needs to contain only the contiguous samples with the same format description as the first sample.

 If there’s a change of format description between the sample cursor and `endSampleCursor`, the returned sample buffer needs to contain only the contiguous samples with the same format description as the first sample.

## Parameters

- `endSampleCursor`: If not  , this cursor indicates the last sample that the new sample buffer should contain.
- `completionHandler`: The completion block to execute when the load operation finishes.

## See Also

- [func chunkDetails() throws -> MESampleCursorChunk](mesamplecursor/chunkdetails.md)
  Returns information about the chunk that holds the sample indicated by the cursor.
- [func sampleLocation() throws -> MESampleLocation](mesamplecursor/samplelocation.md)
  Returns the location and byte source of the sample indicated by the cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:))*