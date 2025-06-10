# SCNMorpherCalculationMode

**Framework**: SceneKit  
**Kind**: enum

The interpolation formulas for blending between target geometries.

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
enum SCNMorpherCalculationMode
```

#### Overview

A morpher computes its current surface by summing weighted geometry elements from the base geometry and all target geometries. The position of a vertex on the surface is produced by adding the position vector of a point on the base geometry to the position vectors of the corresponding points on all target geometries. The morpher’s [`calculationMode`](scnmorpher/calculationmode.md) property selects the formula used to calculate this sum.

If the mode is [`SCNMorpherCalculationMode.normalized`](scnmorphercalculationmode/normalized.md), the position from the base geometry is weighted by one minus the sum of all target weights, as in the following formula:

```objc
Position = (1 - weight0 - weight1 - ...) * Base + weight0 * Target0 + weight1 * Target1 + ...
```

If the mode is [`SCNMorpherCalculationMode.additive`](scnmorphercalculationmode/additive.md), the position from the base geometry is not weighted, and SceneKit uses the following formula instead:

```objc
Position = Base + weight0 * Target0 + weight1 * Target1 + ...
```

## Topics

### Constants
- [SCNMorpherCalculationMode.normalized](scnmorphercalculationmode/normalized.md)
  Target weights must be in the range between `0.0` and `1.0`, and the contribution of the base geometry to the morphed surface is related to the sum of target weights. This is the default mode.
- [SCNMorpherCalculationMode.additive](scnmorphercalculationmode/additive.md)
  Target weights may take on any value, and weighted contributions for each target are added to the base geometry,
### Initializers
- [init?(rawValue: Int)](scnmorphercalculationmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmorphercalculationmode)*