# PortalComponent.Options

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Options to toggle the portal features on and off.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Options
```

## Overview

This option set is equivalent to setting [`clippingMode`](./clippingmode-swift.property.md) and [`crossingMode`](./crossingmode-swift.property.md) directly.

Use this type with [`init(target:plane:options:)`](./init%28target,plane,options%29.md).

## Topics

### Type Properties
- [static let allowCrossing: PortalComponent.Options](./options/allowcrossing.md)
  An option that enables the crossing feature.
- [static let clipContents: PortalComponent.Options](./options/clipcontents.md)
  An option that enables the clipping feature.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/options)*