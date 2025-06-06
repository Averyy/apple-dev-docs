# SCNTransparencyMode

**Framework**: SceneKit  
**Kind**: enum

The modes SceneKit uses to calculate the opacity of pixels rendered with a material, used by the [`transparencyMode`](scnmaterial/transparencymode.md) property.

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
enum SCNTransparencyMode
```

## Topics

### Constants
- [SCNTransparencyMode.aOne](scntransparencymode/aone.md)
  SceneKit derives transparency information from the alpha channel of colors. The value `1.0` is opaque.
- [SCNTransparencyMode.rgbZero](scntransparencymode/rgbzero.md)
  SceneKit derives transparency information from the luminance of colors. The value `0.0` is opaque.
### Enumeration Cases
- [SCNTransparencyMode.dualLayer](scntransparencymode/duallayer.md)
- [SCNTransparencyMode.singleLayer](scntransparencymode/singlelayer.md)
### Initializers
- [init?(rawValue: Int)](scntransparencymode/init(rawvalue:).md)
### Type Properties
- [static var `default`: SCNTransparencyMode](scntransparencymode/default.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var transparency: CGFloat](scnmaterial/transparency.md)
  The uniform transparency of the material. Animatable.
- [var transparencyMode: SCNTransparencyMode](scnmaterial/transparencymode.md)
  The mode SceneKit uses to calculate transparency for the material.
- [var blendMode: SCNBlendMode](scnmaterial/blendmode.md)
  The mode that determines how pixel colors rendered using this material blend with other pixel colors in the rendering target.
- [enum SCNBlendMode](scnblendmode.md)
  Modes that describe how SceneKit blends source colors rendered using a material with destination colors already in a rendering target, used by the [`blendMode`](scnmaterial/blendmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransparencymode)*