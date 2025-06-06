# stepInPresentationOrder(by:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Required**: Yes

Moves the cursor a given number of samples in presentation order.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func stepInPresentationOrder(by stepCount: Int64) async throws -> Int64
```

#### Discussion

If the request would advance the cursor past the last sample or before the first sample, the cursor points to that limiting sample and `actualStepCount` is equal to the number of samples the cursor moved. If decode order and presentation order are the same, in other words, the samples aren’t reordered, this method has the same effect as [`stepInDecodeOrder(byCount:)`](https://developer.apple.com/documentation/AVFoundation/AVSampleCursor/stepInDecodeOrder(byCount:)).

## Parameters

- `stepCount`: The number of samples to move. If positive, the cursor steps forward. If negative, the cursor steps backward.
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
- [func stepByPresentationTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](mesamplecursor/stepbypresentationtime(_:completionhandler:).md)
  Moves the cursor on the presentation timeline by the delta presentation time that you specify.
- [func stepInDecodeOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](mesamplecursor/stepindecodeorder(by:completionhandler:).md)
  Moves the cursor a given number of samples in decode order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/stepinpresentationorder(by:completionhandler:))*