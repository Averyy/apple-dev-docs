# SCNBillboardAxis

**Framework**: SceneKit  
**Kind**: struct

Options for locking the orientation of nodes affected by a billboard constraint.

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
struct SCNBillboardAxis
```

#### Overview

The figure below shows the effects of constraining various axes.

![None](https://docs-assets.developer.apple.com/published/31307ee6cbcf77d7cd5b4367045d24bc/media-2929767%402x.png)

## Topics

### Constants
- [static var X: SCNBillboardAxis](scnbillboardaxis/x.md)
  Align an affected node such that its x-axis is always parallel to that of the view, leaving it free to rotate otherwise.
- [static var Y: SCNBillboardAxis](scnbillboardaxis/y.md)
  Align an affected node such that its y-axis is always parallel to that of the view, leaving it free to rotate otherwise.
- [static var Z: SCNBillboardAxis](scnbillboardaxis/z.md)
  Align an affected node such that its z-axis is always perpendicular to the viewing plane, leaving it free to rotate otherwise.
- [static var all: SCNBillboardAxis](scnbillboardaxis/all.md)
  Align an affected node such that its orientation always matches that of the view.
### Initializers
- [init(rawValue: UInt)](scnbillboardaxis/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbillboardaxis)*