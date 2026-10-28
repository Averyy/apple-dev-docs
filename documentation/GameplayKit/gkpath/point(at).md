# point(at:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Returns the 2D point at the specified index in the path’s list of vertices.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.12
- tvOS 9.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`float2(at:)`](./float2%28at%29.md) method instead.

## Declaration

```swift
func point(at index: Int) -> vector_float2
```

```objc
- (vector_float2) pointAtIndex:(NSUInteger) index;
```

## Return Value

The vertex at the specified index.

## Parameters

- `index`: The index of the vertex to return, between `0` and the [`numPoints`](./numpoints.md) value.

## See Also

### Inspecting a Path’s Shape
- [var numPoints: Int](./numpoints.md)
  The number of vertices in the path.
- [func float2(at: Int) -> vector_float2](./float2%28at%29.md)
  Returns the 2D point at the specified index in the path’s list of vertices.
- [func float3(at: Int) -> vector_float3](./float3%28at%29.md)
  Returns the 3D point at the specified index in the path’s list of vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkpath/point(at:))*