# render(meshInstancesArrayIndex:meshInstanceIndex:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Encodes a draw call for a single mesh instance.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func render(meshInstancesArrayIndex: Int, meshInstanceIndex: Int)
```

## Parameters

- `meshInstancesArrayIndex`: The slot index of the mesh instance array that contains the instance.
- `meshInstanceIndex`: The index of the mesh instance within that array.

## See Also

### Rendering mesh instances
- [func render(meshInstancesArrayIndex: Int, range: Range<Int>)](./render%28meshinstancesarrayindex,range%29.md)
  Encodes draw calls for a contiguous range of mesh instances.
- [func reset()](./reset%28%29.md)
  Resets the render encoder state to renderer defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/renderstate/render(meshinstancesarrayindex:meshinstanceindex:))*