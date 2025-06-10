# controlPointFormat

**Framework**: Metal  
**Kind**: property

Declares the format of the control points the control point buffer references.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var controlPointFormat: MTLAttributeFormat { get set }
```

#### Discussion

Defaults to `MTLAttributeFormatFloat3`, representing 3 floating point values tightly packed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointformat)*