# curveBasis

**Framework**: Metal  
**Kind**: property

Sets the curve basis function, determining how Metal interpolates the control points.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var curveBasis: MTLCurveBasis { get set }
```

#### Discussion

Defaults to `MTLCurveBasisBSpline`. All keyframes share the same curve basis function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/curvebasis)*