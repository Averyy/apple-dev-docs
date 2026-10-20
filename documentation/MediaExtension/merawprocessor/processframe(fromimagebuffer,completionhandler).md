# processFrame(fromImageBuffer:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests the processor to process a video frame.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func processFrame(fromImageBuffer inputFrame: CVPixelBuffer, completionHandler: @escaping @Sendable (CVPixelBuffer?, (any Error)?) -> Void)
```

```swift
func processFrame(fromImageBuffer inputFrame: CVPixelBuffer) async throws -> CVPixelBuffer
```

```objc
- (void) processFrameFromImageBuffer:(CVPixelBufferRef) inputFrame completionHandler:(void (^)(CVPixelBufferRef imageBuffer, NSError *error)) completionHandler;
```

#### Discussion

The completionHandler block must be called for every [`processFrame(fromImageBuffer:completionHandler:)`](./processframe%28fromimagebuffer,completionhandler%29.md) call when processing is complete. The completion handler block should return either a processed pixel buffer or an error.

## Parameters

- `inputFrame`: A CVPixelBuffer that contains a video frame to process.
- `completionHandler`: The handler is invoked when a frame processes and is ready to be sent back to the caller. This block does not need to be called in the order in which frames were submitted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor/processframe(fromimagebuffer:completionhandler:))*