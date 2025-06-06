# PortalComponent.Options

**Framework**: RealityKit  
**Kind**: struct

Options to toggle the portal features on and off.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Options
```

#### Overview

This option set is equivalent to setting [`clippingMode`](portalcomponent/clippingmode-swift.property.md) and [`crossingMode`](portalcomponent/crossingmode-swift.property.md) directly.

Use this type with [`init(target:plane:options:)`](portalcomponent/init(target:plane:options:).md).

## Topics

### Initializers
- [init(rawValue: UInt)](portalcomponent/options/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: UInt](portalcomponent/options/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [PortalComponent.Options.ArrayLiteralElement](portalcomponent/options/arrayliteralelement.md)
  The type of the elements of an array literal.
- [PortalComponent.Options.Element](portalcomponent/options/element.md)
  The element type of the option set.
- [PortalComponent.Options.RawValue](portalcomponent/options/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let allowCrossing: PortalComponent.Options](portalcomponent/options/allowcrossing.md)
  An option that enables the crossing feature.
- [static let clipContents: PortalComponent.Options](portalcomponent/options/clipcontents.md)
  An option that enables the clipping feature.
### Default Implementations
- [Equatable Implementations](portalcomponent/options/equatable-implementations.md)
- [OptionSet Implementations](portalcomponent/options/optionset-implementations.md)
- [SetAlgebra Implementations](portalcomponent/options/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/options)*