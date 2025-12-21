# sheared(_:)

**Framework**: Spatial  
**Kind**: method

Returns a sheared rectangle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func sheared(_ shear: AxisWithFactors) -> Rect3DFloat
```

#### Discussion

- Returns The sheared rectangle.

Because affine transforms do not preserve rectangles in general, this function returns the smallest rectangle that contains the transformed corner points of the rect parameter.

## Parameters

- `shear`: The axis and shear factors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/sheared(_:))*