# particleColorSequence

**Framework**: SpriteKit  
**Kind**: property

The sequence used to specify the color components of a particle over its lifetime.

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
var particleColorSequence: SKKeyframeSequence? { get set }
```

## Mentions

- [Using Keyframe Sequence to effect Custom Interpolation](using-keyframe-sequence-to-effect-custom-interpolation.md)
- [Animating Particle Properties Across Disparate Values](animating-particle-properties-across-disparate-values.md)

#### Discussion

The default value is `nil`. If a non-`nil` value is specified, then the [`particleColor`](skemitternode/particlecolor.md), [`particleColorAlphaRange`](skemitternode/particlecoloralpharange.md), [`particleColorRedRange`](skemitternode/particlecolorredrange.md), [`particleColorGreenRange`](skemitternode/particlecolorgreenrange.md), [`particleColorBlueRange`](skemitternode/particlecolorbluerange.md), [`particleColorAlphaSpeed`](skemitternode/particlecoloralphaspeed.md), [`particleColorRedSpeed`](skemitternode/particlecolorredspeed.md), [`particleColorGreenSpeed`](skemitternode/particlecolorgreenspeed.md), and [`particleColorBlueSpeed`](skemitternode/particlecolorbluespeed.md) properties are ignored. Instead, the sequence is used to specify the particle color.

> ❗ **Important**:  If you create an [`SKEmitterNode`](skemitternode.md) object using Xcode’s particle editor, it uses a color sequence to implement the color change.

 If you create an [`SKEmitterNode`](skemitternode.md) object using Xcode’s particle editor, it uses a color sequence to implement the color change.

## See Also

- [var particleColor: UIColor](skemitternode/particlecolor.md)
  The average initial color for a particle.
- [var particleColorAlphaRange: CGFloat](skemitternode/particlecoloralpharange.md)
  The range of allowed random values for the alpha component of a particle’s initial color.
- [var particleColorBlueRange: CGFloat](skemitternode/particlecolorbluerange.md)
  The range of allowed random values for the blue component of a particle’s initial color.
- [var particleColorGreenRange: CGFloat](skemitternode/particlecolorgreenrange.md)
  The range of allowed random values for the green component of a particle’s initial color.
- [var particleColorRedRange: CGFloat](skemitternode/particlecolorredrange.md)
  The range of allowed random values for the red component of a particle’s initial color.
- [var particleColorAlphaSpeed: CGFloat](skemitternode/particlecoloralphaspeed.md)
  The rate at which the alpha component of a particle’s color changes per second.
- [var particleColorBlueSpeed: CGFloat](skemitternode/particlecolorbluespeed.md)
  The rate at which the blue component of a particle’s color changes per second.
- [var particleColorGreenSpeed: CGFloat](skemitternode/particlecolorgreenspeed.md)
  The rate at which the green component of a particle’s color changes per second.
- [var particleColorRedSpeed: CGFloat](skemitternode/particlecolorredspeed.md)
  The rate at which the red component of a particle’s color changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolorsequence)*