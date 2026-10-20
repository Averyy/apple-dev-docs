# controlPointCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Specifies the number of control points in the buffers the control point buffers reference.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var controlPointCount: Int { get set }
```

```objc
@property (nonatomic) NSUInteger controlPointCount;
```

#### Discussion

All keyframes have the same number of control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/controlpointcount)*