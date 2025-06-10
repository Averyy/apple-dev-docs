# curveBasis

**Framework**: Metal  
**Kind**: property

Sets the curve basis function, determining how Metal interpolates the control points.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var curveBasis: MTLCurveBasis { get set }
```

#### Discussion

Defaults to `MTLCurveBasisBSpline`. All keyframes share the same curve basis function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/curvebasis)*