# chunkDetails()

**Framework**: MediaExtension  
**Kind**: method

Returns information about the chunk that holds the sample indicated by the cursor.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func chunkDetails() throws -> MESampleCursorChunk
```

#### Return Value

A sample cursor chunk.

#### Discussion

If the sample resides in a contiguous chunk of the file among similar samples, this method returns information about that chunk.

> **Note**:  If a cursor implements this method, it also needs to implement [`sampleLocation()`](mesamplecursor/samplelocation().md) to get samples inside the chunk’s location.

It may not be practical to use this method with some media assets. In this case, or if the cursor doesn’t support this method, it returns [`MEError.Code.locationNotAvailable`](meerror-swift.struct/code/locationnotavailable.md), which indicates to use [`loadSampleBufferContainingSamples(to:completionHandler:)`](mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:).md) to load the sample data instead.

## See Also

- [func sampleLocation() throws -> MESampleLocation](mesamplecursor/samplelocation.md)
  Returns the location and byte source of the sample indicated by the cursor.
- [func loadSampleBufferContainingSamples(to: (any MESampleCursor)?, completionHandler: (CMSampleBuffer?, (any Error)?) -> Void)](mesamplecursor/loadsamplebuffercontainingsamples(to:completionhandler:).md)
  Builds a sample buffer that contains the samples at the cursor that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/chunkdetails())*