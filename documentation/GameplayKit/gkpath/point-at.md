# point(at:)

**Framework**: GameplayKit  
**Kind**: method

Returns the 2D point at the specified index in the path’s list of vertices.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func point(at index: Int) -> vector_float2
```

#### Return Value

The vertex at the specified index.

## Parameters

- `index`: The index of the vertex to return, between   and the   value.

## See Also

- [var numPoints: Int](gkpath/numpoints.md)
  The number of vertices in the path.
- [func float2(at: Int) -> vector_float2](gkpath/float2(at:).md)
  Returns the 2D point at the specified index in the path’s list of vertices.
- [func float3(at: Int) -> vector_float3](gkpath/float3(at:).md)
  Returns the 3D point at the specified index in the path’s list of vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpath/point(at:))*