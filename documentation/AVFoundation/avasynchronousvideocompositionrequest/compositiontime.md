# compositionTime

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A time for which to compose the frame.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var compositionTime: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime compositionTime;
```

## See Also

### Inspecting the request
- [var renderContext: AVVideoCompositionRenderContext](./rendercontext.md)
  The rendering context of the video composition.
- [var videoCompositionInstruction: any AVVideoCompositionInstructionProtocol](./videocompositioninstruction.md)
  A video composition instruction that indicates how to compose the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/compositiontime)*