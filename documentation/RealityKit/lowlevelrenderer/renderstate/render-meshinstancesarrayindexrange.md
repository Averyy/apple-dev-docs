# render(meshInstancesArrayIndex:range:)

**Framework**: RealityKit  
**Kind**: method

Encodes draw calls for a contiguous range of mesh instances.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func render(meshInstancesArrayIndex: Int, range: Range<Int>)
```

## Parameters

- `meshInstancesArrayIndex`: The slot index of the mesh instance array that contains the instances.
- `range`: The range of mesh instance indices to draw.

## See Also

- [func render(meshInstancesArrayIndex: Int, meshInstanceIndex: Int)](lowlevelrenderer/renderstate/render(meshinstancesarrayindex:meshinstanceindex:).md)
  Encodes a draw call for a single mesh instance.
- [func reset()](lowlevelrenderer/renderstate/reset.md)
  Resets the render encoder state to renderer defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/renderstate/render(meshinstancesarrayindex:range:))*