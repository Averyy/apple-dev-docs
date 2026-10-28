# particleColorSequence

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The sequence used to specify the color components of a particle over its lifetime.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var particleColorSequence: SKKeyframeSequence? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKKeyframeSequence * particleColorSequence;
```

## Mentions

- [Animating Particle Properties Across Disparate Values](../animating-particle-properties-across-disparate-values.md)
- [Using Keyframe Sequence to effect Custom Interpolation](../using-keyframe-sequence-to-effect-custom-interpolation.md)

## Discussion

The default value is `nil`. If a non-`nil` value is specified, then the [`particleColor`](./particlecolor.md), [`particleColorAlphaRange`](./particlecoloralpharange.md), [`particleColorRedRange`](./particlecolorredrange.md), [`particleColorGreenRange`](./particlecolorgreenrange.md), [`particleColorBlueRange`](./particlecolorbluerange.md), [`particleColorAlphaSpeed`](./particlecoloralphaspeed.md), [`particleColorRedSpeed`](./particlecolorredspeed.md), [`particleColorGreenSpeed`](./particlecolorgreenspeed.md), and [`particleColorBlueSpeed`](./particlecolorbluespeed.md) properties are ignored. Instead, the sequence is used to specify the particle color.

> ❗ **Important**:  If you create an [`SKEmitterNode`](../skemitternode.md) object using Xcode’s particle editor, it uses a color sequence to implement the color change.

## See Also

### Configuring Particle Color
- [var particleColor: UIColor](./particlecolor.md)
  The average initial color for a particle.
- [var particleColorAlphaRange: CGFloat](./particlecoloralpharange.md)
  The range of allowed random values for the alpha component of a particle’s initial color.
- [var particleColorBlueRange: CGFloat](./particlecolorbluerange.md)
  The range of allowed random values for the blue component of a particle’s initial color.
- [var particleColorGreenRange: CGFloat](./particlecolorgreenrange.md)
  The range of allowed random values for the green component of a particle’s initial color.
- [var particleColorRedRange: CGFloat](./particlecolorredrange.md)
  The range of allowed random values for the red component of a particle’s initial color.
- [var particleColorAlphaSpeed: CGFloat](./particlecoloralphaspeed.md)
  The rate at which the alpha component of a particle’s color changes per second.
- [var particleColorBlueSpeed: CGFloat](./particlecolorbluespeed.md)
  The rate at which the blue component of a particle’s color changes per second.
- [var particleColorGreenSpeed: CGFloat](./particlecolorgreenspeed.md)
  The rate at which the green component of a particle’s color changes per second.
- [var particleColorRedSpeed: CGFloat](./particlecolorredspeed.md)
  The rate at which the red component of a particle’s color changes per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolorsequence)*