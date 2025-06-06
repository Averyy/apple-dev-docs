# catmullRom(alpha:)

**Framework**: Swift Charts  
**Kind**: method

Interpolate data points with Catmull-Rom spline, using the given alpha parameter.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func catmullRom(alpha: CGFloat) -> InterpolationMethod
```

## Parameters

- `alpha`: A parameter for the Catmull-Rom spline.   Use 0 for a uniform spline, 0.5 for the centripetal spline,   and 1.0 for the chordal spline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/interpolationmethod/catmullrom(alpha:))*