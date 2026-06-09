# USDPreviewSession.OptimizationSteps

**Framework**: Spatial Preview  
**Kind**: struct

A set of optimization steps to apply to a USD stage before previewing on a device.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct OptimizationSteps
```

## Topics

### Type Properties
- [static let compressed: USDPreviewSession.OptimizationSteps](usdpreviewsession/optimizationsteps/compressed.md)
  Allows the USD stage’s textures and meshes to be compressed before previewing on a device. Reduces the transmission file size of the USD stage by compressing textures and meshes to minimize the data sent, and is only applied when the stage exceeds the compression threshold. Can be combined with `.optimized` — compression runs after the `.optimized` optimization step on the resulting stage.
- [static let optimized: USDPreviewSession.OptimizationSteps](usdpreviewsession/optimizationsteps/optimized.md)
  Allows the USD stage to be analyzed and potentially simplified or replaced with a proxy before previewing on a device. The USD analysis decides at runtime whether the stage can be passed as-is, simplified in place, or swapped for a lower-fidelity proxy based on scene complexity and session capabilities.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/optimizationsteps)*