# reset()

**Framework**: RealityKit  
**Kind**: method

Resets the render encoder state to renderer defaults.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func reset()
```

#### Discussion

Call this after any custom Metal commands that modify the depth stencil state, cull mode, viewports, or scissor rects, to restore the renderer’s expected state before the next draw call.

## See Also

- [func render(meshInstancesArrayIndex: Int, meshInstanceIndex: Int)](lowlevelrenderer/renderstate/render(meshinstancesarrayindex:meshinstanceindex:).md)
  Encodes a draw call for a single mesh instance.
- [func render(meshInstancesArrayIndex: Int, range: Range<Int>)](lowlevelrenderer/renderstate/render(meshinstancesarrayindex:range:).md)
  Encodes draw calls for a contiguous range of mesh instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/renderstate/reset())*