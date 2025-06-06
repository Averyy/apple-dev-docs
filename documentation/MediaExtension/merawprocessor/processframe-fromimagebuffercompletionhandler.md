# processFrame(fromImageBuffer:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Required**: Yes

Requests the processor to process a video frame.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func processFrame(fromImageBuffer inputFrame: CVPixelBuffer) async throws -> CVPixelBuffer
```

#### Discussion

The completionHandler block must be called for every [`processFrame(fromImageBuffer:completionHandler:)`](merawprocessor/processframe(fromimagebuffer:completionhandler:).md) call when processing is complete. The completion handler block should return either a processed pixel buffer or an error.

## Parameters

- `inputFrame`: A CVPixelBuffer that contains a video frame to process.
- `completionHandler`: The handler is invoked when a frame processes and is ready to be sent back to the caller. This block does not need to be called in the order in which frames were submitted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor/processframe(fromimagebuffer:completionhandler:))*