# transparencyMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The mode SceneKit uses to calculate transparency for the material.

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
var transparencyMode: SCNTransparencyMode { get set }
```

```objc
@property (nonatomic) SCNTransparencyMode transparencyMode;
```

## Discussion

The default transparency mode is [`SCNTransparencyMode.aOne`](../scntransparencymode/aone.md). See [`SCNTransparencyMode`](../scntransparencymode.md) for available values and their effects.

## See Also

### Managing Opacity and Blending
- [var transparency: CGFloat](./transparency.md)
  The uniform transparency of the material. Animatable.
- [enum SCNTransparencyMode](../scntransparencymode.md)
  The modes SceneKit uses to calculate the opacity of pixels rendered with a material, used by the [`transparencyMode`](./transparencymode.md) property.
- [var blendMode: SCNBlendMode](./blendmode.md)
  The mode that determines how pixel colors rendered using this material blend with other pixel colors in the rendering target.
- [enum SCNBlendMode](../scnblendmode.md)
  Modes that describe how SceneKit blends source colors rendered using a material with destination colors already in a rendering target, used by the [`blendMode`](./blendmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/transparencymode)*