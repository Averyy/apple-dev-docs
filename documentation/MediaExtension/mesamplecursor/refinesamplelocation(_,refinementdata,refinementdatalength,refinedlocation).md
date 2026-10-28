# refineSampleLocation(_:refinementData:refinementDataLength:refinedLocation:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Produces an exact sample location based on the estimated sample location and refinement data that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func refineSampleLocation(_ estimatedSampleLocation: AVSampleCursorStorageRange, refinementData: UnsafePointer<UInt8>, refinementDataLength: Int, refinedLocation refinedLocationOut: UnsafeMutablePointer<AVSampleCursorStorageRange>) throws
```

```objc
- (BOOL) refineSampleLocation:(AVSampleCursorStorageRange) estimatedSampleLocation refinementData:(const uint8_t *) refinementData refinementDataLength:(size_t) refinementDataLength refinedLocation:(AVSampleCursorStorageRange *) refinedLocationOut error:(NSError **) error;
```

## Discussion

Use [`estimatedSampleLocation()`](./estimatedsamplelocation%28%29.md) to obtain the estimated sample location to pass to this method.

## Parameters

- `estimatedSampleLocation`: The estimated sample location.
- `refinementData`: The refinement data.
- `refinementDataLength`: The length of the refinement data in bytes.
- `refinedLocationOut`: The starting file offset and size of the sample in bytes.

## See Also

### Stepping through samples
- [func samplesWithEarlierDTSsMayHaveLaterPTSs(than: any MESampleCursor) -> Bool](./sampleswithearlierdtssmayhavelaterptss%28than%29.md)
  Tests for an earlier boundary in sample reordering.
- [func samplesWithLaterDTSsMayHaveEarlierPTSs(than: any MESampleCursor) -> Bool](./sampleswithlaterdtssmayhaveearlierptss%28than%29.md)
  Tests for a later boundary in sample reordering.
- [func estimatedSampleLocation() throws -> MEEstimatedSampleLocation](./estimatedsamplelocation%28%29.md)
  Returns an estimate of the sample location indicated by the cursor.
- [func stepByDecodeTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](./stepbydecodetime%28_,completionhandler%29.md)
  Moves the cursor on the decode timeline by the delta decode time that you specify.
- [func stepByPresentationTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](./stepbypresentationtime%28_,completionhandler%29.md)
  Moves the cursor on the presentation timeline by the delta presentation time that you specify.
- [func stepInDecodeOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](./stepindecodeorder%28by,completionhandler%29.md)
  Moves the cursor a given number of samples in decode order.
- [func stepInPresentationOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](./stepinpresentationorder%28by,completionhandler%29.md)
  Moves the cursor a given number of samples in presentation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/refinesamplelocation(_:refinementdata:refinementdatalength:refinedlocation:))*