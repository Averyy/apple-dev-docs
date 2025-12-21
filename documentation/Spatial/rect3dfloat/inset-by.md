# inset(by:)

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
func inset(by dXYZ: Size3DFloat) -> Rect3DFloat
```

#### Discussion

Returns a new rectangle with the size updated by the specified amount and the same center point.

This function returns a new rectangle that’s inset by the specified values on each axis. The origin value is offset by the distance specified by the @p dXYZ parameter.

The size is adjusted by @p (2*dXYZ) , relative to the source rectangle. If the width, height, or depth are positive values, then the rectangle’s size is decreased on that dimension.  If width, height, or depth are negative values, the rectangle’s size is increased on that dimension.

## Parameters

- `dXYZ`: A size structure that specifies the inset amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/inset(by:))*