# isReadyForMoreMediaData

**Framework**: AVFoundation  
**Kind**: property

Indicates the readiness of the receiver to accept more sample buffers.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var isReadyForMoreMediaData: Bool { get }
```

#### Discussion

An object conforming to AVQueuedSampleBufferRendering keeps track of the occupancy levels of its internal queues for the benefit of clients that enqueue sample buffers from non-real-time sources – i.e., clients that can supply sample buffers faster than they are consumed, and so need to decide when to hold back.

Clients enqueueing sample buffers from non-real-time sources may hold off from generating or obtaining more sample buffers to enqueue when the value of readyForMoreMediaData is NO.

It is safe to call enqueueSampleBuffer: when readyForMoreMediaData is NO, but it is a bad idea to enqueue sample buffers without bound.

To help with control of the non-real-time supply of sample buffers, such clients can use -requestMediaDataWhenReadyOnQueue:usingBlock in order to specify a block that the receiver should invoke whenever it’s ready for sample buffers to be appended.

The value of readyForMoreMediaData will often change from NO to YES asynchronously, as previously supplied sample buffers are decoded and rendered.

This property is not key value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/isreadyformoremediadata)*