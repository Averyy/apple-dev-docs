# renderContext

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The rendering context of the video composition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var renderContext: AVVideoCompositionRenderContext { get }
```

```objc
@property (nonatomic, readonly) AVVideoCompositionRenderContext * renderContext;
```

## See Also

### Inspecting the request
- [var compositionTime: CMTime](./compositiontime.md)
  A time for which to compose the frame.
- [var videoCompositionInstruction: any AVVideoCompositionInstructionProtocol](./videocompositioninstruction.md)
  A video composition instruction that indicates how to compose the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/rendercontext)*