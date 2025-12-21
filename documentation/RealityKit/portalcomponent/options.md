# PortalComponent.Options

**Framework**: RealityKit  
**Kind**: struct

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

#### Overview

This option set is equivalent to setting [`clippingMode`](portalcomponent/clippingmode-swift.property.md) and [`crossingMode`](portalcomponent/crossingmode-swift.property.md) directly.

Use this type with [`init(target:plane:options:)`](portalcomponent/init(target:plane:options:).md).

## Topics

### Type Properties
- [static let allowCrossing: PortalComponent.Options](portalcomponent/options/allowcrossing.md)
  An option that enables the crossing feature.
- [static let clipContents: PortalComponent.Options](portalcomponent/options/clipcontents.md)
  An option that enables the clipping feature.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/options)*