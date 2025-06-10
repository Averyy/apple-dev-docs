# SCNMorpherCalculationMode.additive

**Framework**: SceneKit  
**Kind**: case

Target weights may take on any value, and weighted contributions for each target are added to the base geometry,

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case additive
```

## See Also

- [SCNMorpherCalculationMode.normalized](scnmorphercalculationmode/normalized.md)
  Target weights must be in the range between `0.0` and `1.0`, and the contribution of the base geometry to the morphed surface is related to the sum of target weights. This is the default mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmorphercalculationmode/additive)*