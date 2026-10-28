# CMBufferQueueGetEndPresentationTimeStamp(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Gets the greatest end presentation timestamp of a buffer queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMBufferQueueGetEndPresentationTimeStamp(_ queue: CMBufferQueue) -> CMTime
```

```c
extern CMTime CMBufferQueueGetEndPresentationTimeStamp(CMBufferQueueRef queue);
```

## Return Value

Returns the sum of `PresentationTimeStamp` and the individual buffer durations.

## Discussion

This is the maximum end time (PTS + duration) of buffers in the queue.                If the `getPresentationTimeStamp` callback is `NULL`, `kCMTimeInvalid` will                be returned.

## Parameters

- `queue`: `CMBufferQueue` being interrogated.

## See Also

### Inspecting Duration and Timing
- [func CMBufferQueueGetDuration(CMBufferQueue) -> CMTime](./cmbufferqueuegetduration%28_%29.md)
  Gets the duration of a buffer queue.
- [func CMBufferQueueGetMinDecodeTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetmindecodetimestamp%28_%29.md)
  Gets the earliest decode timestamp of a buffer queue.
- [func CMBufferQueueGetFirstDecodeTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetfirstdecodetimestamp%28_%29.md)
  Gets the decode timestamp of the first buffer in a buffer queue.
- [func CMBufferQueueGetMinPresentationTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetminpresentationtimestamp%28_%29.md)
  Gets the earliest presentation timestamp of a buffer queue.
- [func CMBufferQueueGetFirstPresentationTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetfirstpresentationtimestamp%28_%29.md)
  Gets the presentation timestamp of the first buffer in a buffer queue.
- [func CMBufferQueueGetMaxPresentationTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetmaxpresentationtimestamp%28_%29.md)
  Gets the greatest presentation timestamp of a buffer queue.
- [func CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS() -> UnsafePointer<CMBufferCallbacks>](./cmbufferqueuegetcallbacksforsamplebufferssortedbyoutputpts%28%29.md)
  Returns a pointer to a structure that contains callbacks to sort sample buffers by output presentation timestamp.
- [func CMBufferQueueGetCallbacksForUnsortedSampleBuffers() -> UnsafePointer<CMBufferCallbacks>](./cmbufferqueuegetcallbacksforunsortedsamplebuffers%28%29.md)
  Returns a pointer to a callback structure for unsorted sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuegetendpresentationtimestamp(_:))*