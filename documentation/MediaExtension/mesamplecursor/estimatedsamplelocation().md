# estimatedSampleLocation()

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Returns an estimate of the sample location indicated by the cursor.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func estimatedSampleLocation() throws -> MEEstimatedSampleLocation
```

```objc
- (MEEstimatedSampleLocation *) estimatedSampleLocationReturningError:(NSError **) error;
```

## Return Value

An object that provides information about the estimated sample location.

## Discussion

Some formats may need to read some data on a per-sample basis to produce the exact sample location. For these formats, it’s more efficient to read a larger chunk of data that contains both the data to produce the exact sample location and the actual sample data.

> **Note**:  If you implement this method, also implement [`refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)`](./refinesamplelocation%28_,refinementdata,refinementdatalength,refinedlocation%29.md).

Pass the value this method returns to [`refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)`](./refinesamplelocation%28_,refinementdata,refinementdatalength,refinedlocation%29.md) to obtain the exact sample location.

To indicate that refinement isn’t necessary, return a value for [`refinementDataLocation`](../meestimatedsamplelocation/refinementdatalocation.md) that has a zero length. If [`refinementDataLocation`](../meestimatedsamplelocation/refinementdatalocation.md) has a non-zero length, the range for the estimated sample location needs to fully cover the refined range that [`refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)`](./refinesamplelocation%28_,refinementdata,refinementdatalength,refinedlocation%29.md) returns, and the refinement data location.

This method fails with the error [`MEError.Code.locationNotAvailable`](../meerror-swift.struct/code/locationnotavailable.md) if the sample location indicated by the cursor isn’t contiguous or the method isn’t supported. In this case, use [`loadSampleBufferContainingSamples(to:completionHandler:)`](./loadsamplebuffercontainingsamples%28to,completionhandler%29.md) to load the sample data.

## See Also

### Stepping through samples
- [func samplesWithEarlierDTSsMayHaveLaterPTSs(than: any MESampleCursor) -> Bool](./sampleswithearlierdtssmayhavelaterptss%28than%29.md)
  Tests for an earlier boundary in sample reordering.
- [func samplesWithLaterDTSsMayHaveEarlierPTSs(than: any MESampleCursor) -> Bool](./sampleswithlaterdtssmayhaveearlierptss%28than%29.md)
  Tests for a later boundary in sample reordering.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/estimatedsamplelocation())*