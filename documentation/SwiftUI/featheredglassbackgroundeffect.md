# FeatheredGlassBackgroundEffect

**Framework**: SwiftUI  
**Kind**: struct

The feathered glass background effect.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
struct FeatheredGlassBackgroundEffect
```

#### Overview

You can also use [`feathered`](glassbackgroundeffect/feathered.md) to construct this effect.

The layout size of a view with feathered glass background is based on the content size instead of the glass background size. When the glass background is clipped by an outer container, such as VStack or HStack, it can be resolved by incrasing content size, such as content padding, or reducing the feathered glass background size with its padding parameter.

## Topics

### Initializers
- [init()](featheredglassbackgroundeffect/init.md)
  Creates a feathered glassBackground effect.
- [init(padding: CGFloat, softEdgeRadius: CGFloat?)](featheredglassbackgroundeffect/init(padding:softedgeradius:).md)
  Creates a feathered glassBackground effect.

## Relationships

### Conforms To
- [GlassBackgroundEffect](glassbackgroundeffect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/featheredglassbackgroundeffect)*