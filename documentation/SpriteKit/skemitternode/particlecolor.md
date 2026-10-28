# particleColor

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The average initial color for a particle.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
var particleColor: UIColor { get set }
```

*macOS*

```swift
var particleColor: NSColor { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, retain) UIColor * particleColor;
```

*macOS*

```objc
@property (nonatomic, retain) NSColor * particleColor;
```

## Discussion

The default value is `[SKColor clearColor]`.

A particle’s color is blended with the texture using its blend color factor. See [`SKEmitterNode`](../skemitternode.md).

> ❗ **Important**:  If you create an [`SKEmitterNode`](../skemitternode.md) object using Xcode’s particle editor, it uses the [`particleColorSequence`](./particlecolorsequence.md) property to implement the color change. This means that the [`particleColor`](./particlecolor.md) property is ignored.

## See Also

### Configuring Particle Color
- [var particleColorSequence: SKKeyframeSequence?](./particlecolorsequence.md)
  The sequence used to specify the color components of a particle over its lifetime.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecolor)*