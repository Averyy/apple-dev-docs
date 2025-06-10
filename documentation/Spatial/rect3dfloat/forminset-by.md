# formInset(by:)

**Framework**: Spatial  
**Kind**: method

Insets the rectangle by the specified size.

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
mutating func formInset(by dXYZ: Size3DFloat)
```

#### Discussion

This function insets the rectangle by the specified values on each axis. The origin value is offset by the distance specified by the `dXYZ` parameter. The size is adjusted by `(2*dXYZ)`, relative to the source rectangle.

If the width, height, or depth are positive values, then the rectangle’s size is decreased on that dimension.  If width, height, or depth are negative values, the rectangle’s size is increased on that dimension.

## Parameters

- `dXYZ`: The inset amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/forminset(by:))*