# reset()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Resets the render encoder state to renderer defaults.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func reset()
```

## Discussion

Call this after any custom Metal commands that modify the depth stencil state, cull mode, viewports, or scissor rects, to restore the renderer’s expected state before the next draw call.

## See Also

### Rendering mesh instances
- [func render(meshInstancesArrayIndex: Int, meshInstanceIndex: Int)](./render%28meshinstancesarrayindex,meshinstanceindex%29.md)
  Encodes a draw call for a single mesh instance.
- [func render(meshInstancesArrayIndex: Int, range: Range<Int>)](./render%28meshinstancesarrayindex,range%29.md)
  Encodes draw calls for a contiguous range of mesh instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/renderstate/reset())*