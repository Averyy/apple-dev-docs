# blendMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The mode that determines how pixel colors rendered using this material blend with other pixel colors in the rendering target.

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
var blendMode: SCNBlendMode { get set }
```

```objc
@property (nonatomic) SCNBlendMode blendMode;
```

## Discussion

With the default blend mode of [`SCNBlendMode.alpha`](../scnblendmode/alpha.md), materials blend according to their alpha (opacity) values—a pixel rendered with a higher alpha value appears more opaque than one with a lower alpha value. Change this property to create special effects. For example, the [`SCNBlendMode.add`](../scnblendmode/add.md) mode can make objects appear to glow.

## See Also

### Managing Opacity and Blending
- [var transparency: CGFloat](./transparency.md)
  The uniform transparency of the material. Animatable.
- [var transparencyMode: SCNTransparencyMode](./transparencymode.md)
  The mode SceneKit uses to calculate transparency for the material.
- [enum SCNTransparencyMode](../scntransparencymode.md)
  The modes SceneKit uses to calculate the opacity of pixels rendered with a material, used by the [`transparencyMode`](./transparencymode.md) property.
- [enum SCNBlendMode](../scnblendmode.md)
  Modes that describe how SceneKit blends source colors rendered using a material with destination colors already in a rendering target, used by the [`blendMode`](./blendmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/blendmode)*