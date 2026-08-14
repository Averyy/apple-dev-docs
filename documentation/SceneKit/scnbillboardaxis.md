# SCNBillboardAxis

**Framework**: SceneKit  
**Kind**: struct

Options for locking the orientation of nodes affected by a billboard constraint.

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
struct SCNBillboardAxis
```

#### Overview

The figure below shows the effects of constraining various axes.

![None](/images/com.apple.scenekit/media-2929767@2x.png)

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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbillboardaxis)*