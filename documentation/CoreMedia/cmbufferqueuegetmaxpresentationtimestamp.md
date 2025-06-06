# CMBufferQueueGetMaxPresentationTimeStamp(_:)

**Framework**: Core Media  
**Kind**: func

Gets the greatest presentation timestamp of a buffer queue.

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
func CMBufferQueueGetMaxPresentationTimeStamp(_ queue: CMBufferQueue) -> CMTime
```

#### Return Value

The greatest presentation timestamp of the interrogated `CMBufferQueue`.

#### Discussion

If the `getPresentationTimeStamp` callback is `NULL`, `kCMTimeInvalid` will be returned.

## Parameters

- `queue`:   being interrogated.

## See Also

- [func CMBufferQueueGetDuration(CMBufferQueue) -> CMTime](cmbufferqueuegetduration(_:).md)
  Gets the duration of a buffer queue.
- [func CMBufferQueueGetMinDecodeTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetmindecodetimestamp(_:).md)
  Gets the earliest decode timestamp of a buffer queue.
- [func CMBufferQueueGetFirstDecodeTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetfirstdecodetimestamp(_:).md)
  Gets the decode timestamp of the first buffer in a buffer queue.
- [func CMBufferQueueGetMinPresentationTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetminpresentationtimestamp(_:).md)
  Gets the earliest presentation timestamp of a buffer queue.
- [func CMBufferQueueGetFirstPresentationTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetfirstpresentationtimestamp(_:).md)
  Gets the presentation timestamp of the first buffer in a buffer queue.
- [func CMBufferQueueGetEndPresentationTimeStamp(CMBufferQueue) -> CMTime](cmbufferqueuegetendpresentationtimestamp(_:).md)
  Gets the greatest end presentation timestamp of a buffer queue.
- [func CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS() -> UnsafePointer<CMBufferCallbacks>](cmbufferqueuegetcallbacksforsamplebufferssortedbyoutputpts().md)
  Returns a pointer to a structure that contains callbacks to sort sample buffers by output presentation timestamp.
- [func CMBufferQueueGetCallbacksForUnsortedSampleBuffers() -> UnsafePointer<CMBufferCallbacks>](cmbufferqueuegetcallbacksforunsortedsamplebuffers().md)
  Returns a pointer to a callback structure for unsorted sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuegetmaxpresentationtimestamp(_:))*