# sampleBufferReceiver(adding:)

**Framework**: AVFoundation  
**Kind**: method

Adds a renderer to the list of renderers under the synchronizer’s control and returns a sample buffer receiver to enqueue samples.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func sampleBufferReceiver(adding renderer: AVSampleBufferVideoRenderer) -> sending AVSampleBufferVideoRenderer.Receiver
```

#### Return Value

A sample buffer receiver to enqueue samples asynchronously in a detached Task

## Parameters

- `renderer`: The render to be added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/samplebufferreceiver(adding:)-rxap)*