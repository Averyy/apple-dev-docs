# SCNBillboardAxis

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

Options for locking the orientation of nodes affected by a billboard constraint.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
struct SCNBillboardAxis
```

```c
enum SCNBillboardAxis : NSUInteger;
```

## Overview

The figure below shows the effects of constraining various axes.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929767@2x.png)

## Topics

### Constants
- [static var X: SCNBillboardAxis](./scnbillboardaxis/x.md)
  Align an affected node such that its x-axis is always parallel to that of the view, leaving it free to rotate otherwise.
- [static var Y: SCNBillboardAxis](./scnbillboardaxis/y.md)
  Align an affected node such that its y-axis is always parallel to that of the view, leaving it free to rotate otherwise.
- [static var Z: SCNBillboardAxis](./scnbillboardaxis/z.md)
  Align an affected node such that its z-axis is always perpendicular to the viewing plane, leaving it free to rotate otherwise.
- [static var all: SCNBillboardAxis](./scnbillboardaxis/all.md)
  Align an affected node such that its orientation always matches that of the view.
### Initializers
- [init(rawValue: UInt)](./scnbillboardaxis/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbillboardaxis)*