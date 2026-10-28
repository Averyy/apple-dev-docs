# samplesWithLaterDTSsMayHaveEarlierPTSs(than:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Tests for a later boundary in sample reordering.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func samplesWithLaterDTSsMayHaveEarlierPTSs(than cursor: any MESampleCursor) -> Bool
```

```objc
- (BOOL) samplesWithLaterDTSsMayHaveEarlierPTSsThanCursor:(id<MESampleCursor>) cursor;
```

## Return Value

[`true`](../../Swift/true.md) if it’s possible that later samples in decode order can have an earlier presentation timestamp than that of the specified cursor; otherwise [`false`](../../Swift/false.md).

## Discussion

This method tests for a boundary in the reordering from decode order to presentation order. This determines when it’s possible for any sample later in decode order than the current sample to have an earllier presentation time than the current sample of the specified cursor. You can use this test to limit backward scans, such as to start forward playback. For example, with the argument cursor fixed, step the cursor forward until it’s impossible for any later-in-decode-order samples to be earlier-in-presentation-order than the argument cursor sample.

Don’t implement this method for formats where sample reordering doesn’t make sense for the track content, which also indicates that the samples aren’t reordered.

> ❗ **Important**:  Only pass a cursor to this method that references the same sequence of samples as the cursor you call this method on, such as that the same instance of [`METrackReader`](../metrackreader.md) created. Otherwise, the result is undefined.

## Parameters

- `cursor`: A sample cursor to use to test the sample reordering boundary.

## See Also

### Stepping through samples
- [func samplesWithEarlierDTSsMayHaveLaterPTSs(than: any MESampleCursor) -> Bool](./sampleswithearlierdtssmayhavelaterptss%28than%29.md)
  Tests for an earlier boundary in sample reordering.
- [func estimatedSampleLocation() throws -> MEEstimatedSampleLocation](./estimatedsamplelocation%28%29.md)
  Returns an estimate of the sample location indicated by the cursor.
- [func refineSampleLocation(AVSampleCursorStorageRange, refinementData: UnsafePointer<UInt8>, refinementDataLength: Int, refinedLocation: UnsafeMutablePointer<AVSampleCursorStorageRange>) throws](./refinesamplelocation%28_,refinementdata,refinementdatalength,refinedlocation%29.md)
  Produces an exact sample location based on the estimated sample location and refinement data that you specify.
- [func stepByDecodeTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](./stepbydecodetime%28_,completionhandler%29.md)
  Moves the cursor on the decode timeline by the delta decode time that you specify.
- [func stepByPresentationTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](./stepbypresentationtime%28_,completionhandler%29.md)
  Moves the cursor on the presentation timeline by the delta presentation time that you specify.
- [func stepInDecodeOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](./stepindecodeorder%28by,completionhandler%29.md)
  Moves the cursor a given number of samples in decode order.
- [func stepInPresentationOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](./stepinpresentationorder%28by,completionhandler%29.md)
  Moves the cursor a given number of samples in presentation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/sampleswithlaterdtssmayhaveearlierptss(than:))*