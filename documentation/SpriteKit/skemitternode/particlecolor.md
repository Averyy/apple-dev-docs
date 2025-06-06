# particleColor

**Framework**: SpriteKit  
**Kind**: property

The average initial color for a particle.

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
@MainActor
var particleColor: NSColor { get set }
```

#### Discussion

The default value is `[SKColor clearColor]`.

A particle’s color is blended with the texture using its blend color factor. See [`SKEmitterNode`](skemitternode.md).

> ❗ **Important**:  If you create an [`SKEmitterNode`](skemitternode.md) object using Xcode’s particle editor, it uses the [`particleColorSequence`](skemitternode/particlecolorsequence.md) property to implement the color change. This means that the [`particleColor`](skemitternode/particlecolor.md) property is ignored.

 If you create an [`SKEmitterNode`](skemitternode.md) object using Xcode’s particle editor, it uses the [`particleColorSequence`](skemitternode/particlecolorsequence.md) property to implement the color change. This means that the [`particleColor`](skemitternode/particlecolor.md) property is ignored.

## See Also

- [var particleColorSequence: SKKeyframeSequence?](skemitternode/particlecolorsequence.md)
  The sequence used to specify the color components of a particle over its lifetime.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolor)*