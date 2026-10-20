# CMBufferQueueGetDuration(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Gets the duration of a buffer queue.

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
func CMBufferQueueGetDuration(_ queue: CMBufferQueue) -> CMTime
```

```c
extern CMTime CMBufferQueueGetDuration(CMBufferQueueRef queue);
```

#### Return Value

Returns sum of all the individual buffer durations in the `CMBufferQueue`.

#### Discussion

The duration of the `CMBufferQueue` is the sum of all the individual                buffer durations, as reported by the `getDuration` callback (provided to                `Creating Buffer Queues`).  If there are no buffers in the queue,                `kCMTimeZero` will be returned.

## Parameters

- `queue`: `CMBufferQueue` being interrogated.

## See Also

### Inspecting Duration and Timing
- [func CMBufferQueueGetMinDecodeTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetmindecodetimestamp%28_%29.md)
  Gets the earliest decode timestamp of a buffer queue.
- [func CMBufferQueueGetFirstDecodeTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetfirstdecodetimestamp%28_%29.md)
  Gets the decode timestamp of the first buffer in a buffer queue.
- [func CMBufferQueueGetMinPresentationTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetminpresentationtimestamp%28_%29.md)
  Gets the earliest presentation timestamp of a buffer queue.
- [func CMBufferQueueGetFirstPresentationTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetfirstpresentationtimestamp%28_%29.md)
  Gets the presentation timestamp of the first buffer in a buffer queue.
- [func CMBufferQueueGetEndPresentationTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetendpresentationtimestamp%28_%29.md)
  Gets the greatest end presentation timestamp of a buffer queue.
- [func CMBufferQueueGetMaxPresentationTimeStamp(CMBufferQueue) -> CMTime](./cmbufferqueuegetmaxpresentationtimestamp%28_%29.md)
  Gets the greatest presentation timestamp of a buffer queue.
- [func CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS() -> UnsafePointer<CMBufferCallbacks>](./cmbufferqueuegetcallbacksforsamplebufferssortedbyoutputpts%28%29.md)
  Returns a pointer to a structure that contains callbacks to sort sample buffers by output presentation timestamp.
- [func CMBufferQueueGetCallbacksForUnsortedSampleBuffers() -> UnsafePointer<CMBufferCallbacks>](./cmbufferqueuegetcallbacksforunsortedsamplebuffers%28%29.md)
  Returns a pointer to a callback structure for unsorted sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuegetduration(_:))*