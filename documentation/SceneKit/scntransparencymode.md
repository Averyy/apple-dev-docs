# SCNTransparencyMode

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

The modes SceneKit uses to calculate the opacity of pixels rendered with a material, used by the [`transparencyMode`](./scnmaterial/transparencymode.md) property.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
enum SCNTransparencyMode
```

```c
enum SCNTransparencyMode : NSInteger;
```

## Topics

### Constants
- [SCNTransparencyMode.aOne](./scntransparencymode/aone.md)
  SceneKit derives transparency information from the alpha channel of colors. The value `1.0` is opaque.
- [SCNTransparencyMode.rgbZero](./scntransparencymode/rgbzero.md)
  SceneKit derives transparency information from the luminance of colors. The value `0.0` is opaque.
### Enumeration Cases
- [SCNTransparencyMode.dualLayer](./scntransparencymode/duallayer.md)
- [SCNTransparencyMode.singleLayer](./scntransparencymode/singlelayer.md)
### Initializers
- [init?(rawValue: Int)](./scntransparencymode/init%28rawvalue%29.md)
### Type Properties
- [static var `default`: SCNTransparencyMode](./scntransparencymode/default.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing Opacity and Blending
- [var transparency: CGFloat](./scnmaterial/transparency.md)
  The uniform transparency of the material. Animatable.
- [var transparencyMode: SCNTransparencyMode](./scnmaterial/transparencymode.md)
  The mode SceneKit uses to calculate transparency for the material.
- [var blendMode: SCNBlendMode](./scnmaterial/blendmode.md)
  The mode that determines how pixel colors rendered using this material blend with other pixel colors in the rendering target.
- [enum SCNBlendMode](./scnblendmode.md)
  Modes that describe how SceneKit blends source colors rendered using a material with destination colors already in a rendering target, used by the [`blendMode`](./scnmaterial/blendmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransparencymode)*