# sheared(_:)

**Framework**: Spatial  
**Kind**: method

Returns a sheared rectangle.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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