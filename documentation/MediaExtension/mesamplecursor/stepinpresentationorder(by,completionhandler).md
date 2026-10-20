# stepInPresentationOrder(by:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Moves the cursor a given number of samples in presentation order.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func stepInPresentationOrder(by stepCount: Int64, completionHandler: @escaping @Sendable (Int64, (any Error)?) -> Void)
```

```swift
func stepInPresentationOrder(by stepCount: Int64) async throws -> Int64
```

```objc
- (void) stepInPresentationOrderByCount:(int64_t) stepCount completionHandler:(void (^)(int64_t actualStepCount, NSError *error)) completionHandler;
```

#### Discussion

If the request would advance the cursor past the last sample or before the first sample, the cursor points to that limiting sample and `actualStepCount` is equal to the number of samples the cursor moved. If decode order and presentation order are the same, in other words, the samples aren’t reordered, this method has the same effect as [`stepInDecodeOrder(byCount:)`](../../AVFoundation/avsamplecursor/stepindecodeorder%28bycount%29.md).

## Parameters

- `stepCount`: The number of samples to move. If positive, the cursor steps forward. If negative, the cursor steps backward.
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
- [func stepByPresentationTime(CMTime, completionHandler: (CMTime, Bool, (any Error)?) -> Void)](./stepbypresentationtime%28_,completionhandler%29.md)
  Moves the cursor on the presentation timeline by the delta presentation time that you specify.
- [func stepInDecodeOrder(by: Int64, completionHandler: (Int64, (any Error)?) -> Void)](./stepindecodeorder%28by,completionhandler%29.md)
  Moves the cursor a given number of samples in decode order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/stepinpresentationorder(by:completionhandler:))*