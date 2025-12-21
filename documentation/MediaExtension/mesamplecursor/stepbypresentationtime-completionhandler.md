# stepByPresentationTime(_:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Required**: Yes

Moves the cursor on the presentation timeline by the delta presentation time that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func stepByPresentationTime(_ deltaPresentationTime: CMTime) async throws -> (CMTime, Bool)
```

#### Discussion

The value for `actualDecodeTime` is the final cursor presentation time. Because sample cursors snap to sample boundaries when stepped, this value may not be equal to the current sample decode time + `deltaPresentationTime`, even if the cursor isn’t pinned.

If the request would advance the cursor past the end of the last sample or before the first sample, this method sets the cursor to point to that limiting sample, and sets `positionWasPinned` to [`true`](https://developer.apple.com/documentation/Swift/true). Otherwise, it sets `positionWasPinned` to [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `deltaPresentationTime`: The presentation time to move the sample cursor to.
- `completionHandler`: The completion block to execute when the move operation finishes.

## See Also

- [func samplesWithEarlierDTSsMayHaveLaterPTSs(than: any MESampleCursor) -> Bool](mesamplecursor/sampleswithearlierdtssmayhavelaterptss(than:).md)
  Tests for an earlier boundary in sample reordering.
- [func samplesWithLaterDTSsMayHaveEarlierPTSs(than: any MESampleCursor) -> Bool](mesamplecursor/sampleswithlaterdtssmayhaveearlierptss(than:).md)
  Tests for a later boundary in sample reordering.
- [func estimatedSampleLocation() throws -> MEEstimatedSampleLocation](mesamplecursor/estimatedsamplelocation.md)
  Returns an estimate of the sample location indicated by the cursor.
- [func refineSampleLocation(AVSampleCursorStorageRange, refinementData: UnsafePointer<UInt8>, refinementDataLength: Int, refinedLocation: UnsafeMutablePointer<AVSampleCursorStorageRange>) throws](mesamplecursor/refinesamplelocation(_:refinementdata:refinementdatalength:refinedlocation:).md)
  Produces an exact sample location based on the estimated sample location and refinement data that you specify.
- [func stepByDecodeTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](mesamplecursor/stepbydecodetime(_:completionhandler:).md)
  Moves the cursor on the decode timeline by the delta decode time that you specify.
- [func stepInDecodeOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](mesamplecursor/stepindecodeorder(by:completionhandler:).md)
  Moves the cursor a given number of samples in decode order.
- [func stepInPresentationOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](mesamplecursor/stepinpresentationorder(by:completionhandler:).md)
  Moves the cursor a given number of samples in presentation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/stepbypresentationtime(_:completionhandler:))*