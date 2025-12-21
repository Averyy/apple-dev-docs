# controlPointFormat

**Framework**: Metal  
**Kind**: property

Declares the format of the control points the control point buffer references.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var controlPointFormat: MTLAttributeFormat { get set }
```

#### Discussion

Defaults to `MTLAttributeFormatFloat3`, representing 3 floating point values tightly packed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointformat)*