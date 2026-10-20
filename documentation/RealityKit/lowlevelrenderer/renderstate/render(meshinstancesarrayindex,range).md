# render(meshInstancesArrayIndex:range:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Encodes draw calls for a contiguous range of mesh instances.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func render(meshInstancesArrayIndex: Int, range: Range<Int>)
```

## Parameters

- `meshInstancesArrayIndex`: The slot index of the mesh instance array that contains the instances.
- `range`: The range of mesh instance indices to draw.

## See Also

### Rendering mesh instances
- [func render(meshInstancesArrayIndex: Int, meshInstanceIndex: Int)](./render%28meshinstancesarrayindex,meshinstanceindex%29.md)
  Encodes a draw call for a single mesh instance.
- [func reset()](./reset%28%29.md)
  Resets the render encoder state to renderer defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/renderstate/render(meshinstancesarrayindex:range:))*