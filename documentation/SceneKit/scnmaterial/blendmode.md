# blendMode

**Framework**: SceneKit  
**Kind**: property

The mode that determines how pixel colors rendered using this material blend with other pixel colors in the rendering target.

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
var blendMode: SCNBlendMode { get set }
```

#### Discussion

With the default blend mode of [`SCNBlendMode.alpha`](scnblendmode/alpha.md), materials blend according to their alpha (opacity) values—a pixel rendered with a higher alpha value appears more opaque than one with a lower alpha value. Change this property to create special effects. For example, the [`SCNBlendMode.add`](scnblendmode/add.md) mode can make objects appear to glow.

## See Also

- [var transparency: CGFloat](scnmaterial/transparency.md)
  The uniform transparency of the material. Animatable.
- [var transparencyMode: SCNTransparencyMode](scnmaterial/transparencymode.md)
  The mode SceneKit uses to calculate transparency for the material.
- [enum SCNTransparencyMode](scntransparencymode.md)
  The modes SceneKit uses to calculate the opacity of pixels rendered with a material, used by the [`transparencyMode`](scnmaterial/transparencymode.md) property.
- [enum SCNBlendMode](scnblendmode.md)
  Modes that describe how SceneKit blends source colors rendered using a material with destination colors already in a rendering target, used by the [`blendMode`](scnmaterial/blendmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/blendmode)*