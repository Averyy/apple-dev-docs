# SCNMorpherCalculationMode.normalized

**Framework**: SceneKit  
**Kind**: case

Target weights must be in the range between `0.0` and `1.0`, and the contribution of the base geometry to the morphed surface is related to the sum of target weights. This is the default mode.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case normalized
```

## See Also

- [SCNMorpherCalculationMode.additive](scnmorphercalculationmode/additive.md)
  Target weights may take on any value, and weighted contributions for each target are added to the base geometry,


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmorphercalculationmode/normalized)*