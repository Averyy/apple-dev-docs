# integral

**Framework**: Spatial  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var integral: Rect3DFloat { get }
```

#### Discussion

A rectangle with the smallest integer values for its origin and size that contains the source rectangle. That is, given a rectangle with fractional origin or size values, integral rounds the rectangle’s origin downward and its size upward to the nearest whole integers, such that the result contains the original rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat/integral)*