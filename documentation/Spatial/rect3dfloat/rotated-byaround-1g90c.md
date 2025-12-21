# rotated(by:around:)

**Framework**: Spatial  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func rotated(by rotation: Rotation3DFloat, around pivot: Point3DFloat) -> Rect3DFloat
```

#### Return Value

A point that’s rotated by the specified rotation.

#### Discussion

Returns a rectangle that’s rotated by a rotation around a specified pivot.

## Parameters

- `rotation`: The rotation.
- `pivot`: The center of rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/rotated(by:around:)-1g90c)*