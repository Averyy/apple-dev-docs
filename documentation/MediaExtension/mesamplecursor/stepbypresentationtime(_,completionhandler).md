# stepByPresentationTime(_:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Moves the cursor on the presentation timeline by the delta presentation time that you specify.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func stepByPresentationTime(_ deltaPresentationTime: CMTime, completionHandler: @escaping @Sendable (CMTime, Bool, (any Error)?) -> Void)
```

```swift
func stepByPresentationTime(_ deltaPresentationTime: CMTime) async throws -> (CMTime, Bool)
```

```objc
- (void) stepByPresentationTime:(CMTime) deltaPresentationTime completionHandler:(void (^)(CMTime actualPresentationTime, BOOL positionWasPinned, NSError *error)) completionHandler;
```

#### Discussion

The value for `actualDecodeTime` is the final cursor presentation time. Because sample cursors snap to sample boundaries when stepped, this value may not be equal to the current sample decode time + `deltaPresentationTime`, even if the cursor isn’t pinned.

If the request would advance the cursor past the end of the last sample or before the first sample, this method sets the cursor to point to that limiting sample, and sets `positionWasPinned` to [`true`](../../Swift/true.md). Otherwise, it sets `positionWasPinned` to [`false`](../../Swift/false.md).

## Parameters

- `deltaPresentationTime`: The presentation time to move the sample cursor to.
- `completionHandler`: The completion block to execute when the move operation finishes.

## See Also

### Stepping through samples
- [func samplesWithEarlierDTSsMayHaveLaterPTSs(than: any MESampleCursor) -> Bool](./sampleswithearlierdtssmayhavelaterptss%28than%29.md)
  Tests for an earlier boundary in sample reordering.
- [func samplesWithLaterDTSsMayHaveEarlierPTSs(than: any MESampleCursor) -> Bool](./sampleswithlaterdtssmayhaveearlierptss%28than%29.md)
  Tests for a later boundary in sample reordering.
- [func estimatedSampleLocation() throws -> MEEstimatedSampleLocation](./estimatedsamplelocation%28%29.md)
  Returns an estimate of the sample location indicated by the cursor.
- [func refineSampleLocation(AVSampleCursorStorageRange, refinementData: UnsafePointer<UInt8>, refinementDataLength: Int, refinedLocation: UnsafeMutablePointer<AVSampleCursorStorageRange>) throws](./refinesamplelocation%28_,refinementdata,refinementdatalength,refinedlocation%29.md)
  Produces an exact sample location based on the estimated sample location and refinement data that you specify.
- [func stepByDecodeTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](./stepbydecodetime%28_,completionhandler%29.md)
  Moves the cursor on the decode timeline by the delta decode time that you specify.
- [func stepInDecodeOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](./stepindecodeorder%28by,completionhandler%29.md)
  Moves the cursor a given number of samples in decode order.
- [func stepInPresentationOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](./stepinpresentationorder%28by,completionhandler%29.md)
  Moves the cursor a given number of samples in presentation order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/stepbypresentationtime(_:completionhandler:))*