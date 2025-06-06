# samplesWithEarlierDTSsMayHaveLaterPTSs(than:)

**Framework**: MediaExtension  
**Kind**: method

Tests for an earlier boundary in sample reordering.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func samplesWithEarlierDTSsMayHaveLaterPTSs(than cursor: any MESampleCursor) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if it’s possible that earlier samples in decode order can have a later presentation timestamp than that of the specified cursor; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method tests for a boundary in the reordering from decode order to presentation order. This determines when it’s possible for any sample earlier in decode order than the current sample to have a later presentation time than the current sample of the specified cursor. You can use this test to limit backward scans, such as to start forward playback. For example, with the argument cursor fixed, step the cursor backward until it’s impossible for any earlier-in-decode-order samples to be later-in-presentation-order than the argument cursor sample.

Don’t implement this method for formats where sample reordering doesn’t make sense for the track content, which also indicates that the samples aren’t reordered.

> ❗ **Important**:  Only pass a cursor to this method that references the same sequence of samples as the cursor you call this method on, such as that the same instance of [`METrackReader`](metrackreader.md) created. Otherwise, the result is undefined.

 Only pass a cursor to this method that references the same sequence of samples as the cursor you call this method on, such as that the same instance of [`METrackReader`](metrackreader.md) created. Otherwise, the result is undefined.

## Parameters

- `cursor`: A sample cursor to use to test the sample reordering boundary.

## See Also

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
- [func stepInPresentationOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](mesamplecursor/stepinpresentationorder(by:completionhandler:).md)
  Moves the cursor a given number of samples in presentation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/sampleswithearlierdtssmayhavelaterptss(than:))*