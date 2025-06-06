# transparencyMode

**Framework**: SceneKit  
**Kind**: property

The mode SceneKit uses to calculate transparency for the material.

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
var transparencyMode: SCNTransparencyMode { get set }
```

#### Discussion

The default transparency mode is [`SCNTransparencyMode.aOne`](scntransparencymode/aone.md). See [`SCNTransparencyMode`](scntransparencymode.md) for available values and their effects.

## See Also

- [var transparency: CGFloat](scnmaterial/transparency.md)
  The uniform transparency of the material. Animatable.
- [enum SCNTransparencyMode](scntransparencymode.md)
  The modes SceneKit uses to calculate the opacity of pixels rendered with a material, used by the [`transparencyMode`](scnmaterial/transparencymode.md) property.
- [var blendMode: SCNBlendMode](scnmaterial/blendmode.md)
  The mode that determines how pixel colors rendered using this material blend with other pixel colors in the rendering target.
- [enum SCNBlendMode](scnblendmode.md)
  Modes that describe how SceneKit blends source colors rendered using a material with destination colors already in a rendering target, used by the [`blendMode`](scnmaterial/blendmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/transparencymode)*