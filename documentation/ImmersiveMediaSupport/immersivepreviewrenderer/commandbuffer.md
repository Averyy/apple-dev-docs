# commandBuffer

**Framework**: Immersive Media Support  
**Kind**: property

The command buffer of the render.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
var commandBuffer: (any MTLCommandBuffer)? { get }
```

#### Discussion

Use this to present a drawable and commit the command buffer to finalize the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivepreviewrenderer/commandbuffer)*