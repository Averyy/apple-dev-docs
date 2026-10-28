# curveEndCaps

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Configures the type of curve end caps.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var curveEndCaps: MTLCurveEndCaps { get set }
```

```objc
@property (nonatomic) MTLCurveEndCaps curveEndCaps;
```

## Discussion

Defaults to `MTLCurveEndCapsNone`. All keyframes share the same end cap type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuremotioncurvegeometrydescriptor/curveendcaps)*