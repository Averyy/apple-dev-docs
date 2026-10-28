# integral

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

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
var integral: Rect3DFloat { get }
```

```c
static SPRect3DFloat SPRect3DFloatIntegral(SPRect3DFloat rect);
```

## Discussion

Returns the smallest rectangle with integer coordinates that contains the source rectangle.

A rectangle with the smallest integer values for its origin and size that contains the source rectangle. That is, given a rectangle with fractional origin or size values, integral rounds the rectangle’s origin downward and its size upward to the nearest whole integers, such that the result contains the original rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/integral)*