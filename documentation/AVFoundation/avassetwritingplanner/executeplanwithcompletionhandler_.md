# executePlanWithCompletionHandler:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Starts the incremental segment writing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (void) executePlanWithCompletionHandler:(void (^)(AVComposition *assemblyComposition, NSError *error)) completionHandler;
```

## Discussion

The planner calls the writingSegmentCallbackBlock sequentially, starting with the first segment work, or at the next unfinished segment if resuming a previously suspended session. The completionHandler is called upon failure or success. When called with success (error is nil), this means that all segments for all tracks have been completed. The assemblyComposition will be non-nil and can be used to put the incremental tracks back together. One way to accomplish this is by feeding the assemblyComposition through AVAssetExportSession with the pass-through preset. The client is responsible for combining any other tracks (those that were not eligible for incremental writing), as well as establishing any track references between the incrementally written tracks and the other tracks in the final asset.

## Parameters

- `completionHandler`: Called when all the incremental segments on all tracks added to the planner have completed, or some error occurs.

## See Also

### Executing the plan
- [- executePlanOnQueue:withCompletionHandler:](./executeplanonqueue_withcompletionhandler_.md)
  Starts the incremental segment writing on a given dispatch queue


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwritingplanner/executeplanwithcompletionhandler:)*