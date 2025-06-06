# base

**Framework**: Model I/O  
**Kind**: property

Another material object from which this material’s properties are derived.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var base: MDLMaterial? { get set }
```

#### Discussion

When you use the [`property(with:)`](mdlmaterial/property(with:).md), [`propertyNamed(_:)`](mdlmaterial/propertynamed(_:).md), or [`subscript(_:)`](mdlmaterial/subscript(_:)-323j3.md) method to access material properties, the [`MDLMaterial`](mdlmaterial.md) class first checks whether the material itself has a material property with the specified name or semantic. If not, those methods forward to the corresponding method of the other [`MDLMaterial`](mdlmaterial.md) object specified by this property.

Use this method to create sets of materials that share most of their material properties but differ in others. For example, you can have a set of objects in the same scene with the same general style of surface appearance (determined by the [`scatteringFunction`](mdlmaterial/scatteringfunction.md) property) but with different values for the [`baseColor`](mdlscatteringfunction/basecolor.md) material property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/base)*