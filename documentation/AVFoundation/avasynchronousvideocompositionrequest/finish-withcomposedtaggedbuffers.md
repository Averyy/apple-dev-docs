# finish(withComposedTaggedBuffers:)

**Framework**: AVFoundation  
**Kind**: method

The method that the custom compositor calls when composition succeeds.  - Parameter taggedBuffers: The tagged buffers containing the composed tagged buffers. The tagged buffers must be compatible with the outputBufferDescription specified in the video composition. The outputBufferDescription must not be nil when calling this function.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func finish(withComposedTaggedBuffers taggedBuffers: [CMTaggedDynamicBuffer])
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/finish(withcomposedtaggedbuffers:))*