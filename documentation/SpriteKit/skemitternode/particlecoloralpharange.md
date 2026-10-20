# particleColorAlphaRange

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The range of allowed random values for the alpha component of a particle’s initial color.

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
var particleColorAlphaRange: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat particleColorAlphaRange;
```

#### Discussion

The default value is `0.0`. If non-zero, the starting alpha component of a particle’s color is randomly determined and may vary by plus or minus half of the range value.

## See Also

### Configuring Particle Color
- [var particleColorSequence: SKKeyframeSequence?](./particlecolorsequence.md)
  The sequence used to specify the color components of a particle over its lifetime.
- [var particleColor: UIColor](./particlecolor.md)
  The average initial color for a particle.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlecoloralpharange)*