# render(meshInstancesArrayIndex:meshInstanceIndex:)

**Framework**: RealityKit  
**Kind**: method

Encodes a draw call for a single mesh instance.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func render(meshInstancesArrayIndex: Int, meshInstanceIndex: Int)
```

## Parameters

- `meshInstancesArrayIndex`: The slot index of the mesh instance array that contains the instance.
- `meshInstanceIndex`: The index of the mesh instance within that array.

## See Also

- [func render(meshInstancesArrayIndex: Int, range: Range<Int>)](lowlevelrenderer/renderstate/render(meshinstancesarrayindex:range:).md)
  Encodes draw calls for a contiguous range of mesh instances.
- [func reset()](lowlevelrenderer/renderstate/reset.md)
  Resets the render encoder state to renderer defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/renderstate/render(meshinstancesarrayindex:meshinstanceindex:))*