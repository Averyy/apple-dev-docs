# SCNBlendMode

**Framework**: SceneKit  
**Kind**: enum

Modes that describe how SceneKit blends source colors rendered using a material with destination colors already in a rendering target, used by the [`blendMode`](scnmaterial/blendmode.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SCNBlendMode
```

## Topics

### Constants
- [SCNBlendMode.alpha](scnblendmode/alpha.md)
  Blend by multiplying source and destination color values by their corresponding alpha values.
- [SCNBlendMode.add](scnblendmode/add.md)
  Blend by adding the source color to the destination color.
- [SCNBlendMode.subtract](scnblendmode/subtract.md)
  Blend by subtracting the source color from the destination color.
- [SCNBlendMode.multiply](scnblendmode/multiply.md)
  Blend by multiplying the source color with the background color.
- [SCNBlendMode.screen](scnblendmode/screen.md)
  Blend by multiplying the inverse of the source color with the inverse of the destination color.
- [SCNBlendMode.replace](scnblendmode/replace.md)
  Blend by replacing the destination color with the source color, ignoring alpha.
### Enumeration Cases
- [SCNBlendMode.max](scnblendmode/max.md)
### Initializers
- [init?(rawValue: Int)](scnblendmode/init(rawvalue:).md)

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
- [enum SCNTransparencyMode](scntransparencymode.md)
  The modes SceneKit uses to calculate the opacity of pixels rendered with a material, used by the [`transparencyMode`](scnmaterial/transparencymode.md) property.
- [var blendMode: SCNBlendMode](scnmaterial/blendmode.md)
  The mode that determines how pixel colors rendered using this material blend with other pixel colors in the rendering target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnblendmode)*