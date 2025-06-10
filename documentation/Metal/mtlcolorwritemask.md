# MTLColorWriteMask

**Framework**: Metal  
**Kind**: struct

Values used to specify a mask to permit or restrict writing to color channels of a color value. The values [`red`](mtlcolorwritemask/red.md), [`green`](mtlcolorwritemask/green.md), [`blue`](mtlcolorwritemask/blue.md), and [`alpha`](mtlcolorwritemask/alpha.md) select one color channel each, and they can be bitwise combined.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
struct MTLColorWriteMask
```

## Topics

### Initializers
- [init(rawValue: UInt)](mtlcolorwritemask/init(rawvalue:).md)
  Returns a new color write mask from a specified raw value.
### Constants
- [static var red: MTLColorWriteMask](mtlcolorwritemask/red.md)
  The red color channel is enabled.
- [static var green: MTLColorWriteMask](mtlcolorwritemask/green.md)
  The green color channel is enabled.
- [static var blue: MTLColorWriteMask](mtlcolorwritemask/blue.md)
  The blue color channel is enabled.
- [static var alpha: MTLColorWriteMask](mtlcolorwritemask/alpha.md)
  The alpha color channel is enabled.
- [static var all: MTLColorWriteMask](mtlcolorwritemask/all.md)
  All color channels are enabled.
### Type Properties
- [static var unspecialized: MTLColorWriteMask](mtlcolorwritemask/unspecialized.md)
  Defers assigning the color write mask.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [enum MTLBlendOperation](mtlblendoperation.md)
  For every pixel, `MTLBlendOperation` determines how to combine and weight the source fragment values with the destination values. Some blend operations multiply the source values by a source blend factor (SBF), multiply the destination values by a destination blend factor (DBF), and then combine the results using addition or subtraction. Other blend operations use either a minimum or maximum function to determine the result.
- [enum MTLBlendFactor](mtlblendfactor.md)
  The source and destination blend factors are often needed to complete specification of a blend operation. In most cases, the blend factor for both RGB values () and alpha values () are similar to one another, but in some cases, such as `MTLBlendFactorSourceAlphaSaturated`, the blend factor is slightly different. Four blend factors (`MTLBlendFactorBlendColor`, `MTLBlendFactorOneMinusBlendColor`, `MTLBlendFactorBlendAlpha`, and `MTLBlendFactorOneMinusBlendAlpha`) refer to a constant blend color value that is set by the [`setBlendColor(red:green:blue:alpha:)`](mtlrendercommandencoder/setblendcolor(red:green:blue:alpha:).md) method of `MTLRenderCommandEncoder`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcolorwritemask)*