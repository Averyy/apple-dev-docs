# transparency

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The uniform transparency of the material. Animatable.

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
var transparency: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat transparency;
```

## Discussion

SceneKit determines the total opacity of each rendered pixel in a surface by multiplying the color from the material’s [`transparent`](./transparent.md) property by the value of this property. Then, the material’s [`transparencyMode`](./transparencymode.md) property determines how pixels from the material are blended into the scene.

You can also uniformly adjust the opacity of all content attached to a node using its [`opacity`](../scnnode/opacity.md) property.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing Opacity and Blending
- [var transparencyMode: SCNTransparencyMode](./transparencymode.md)
  The mode SceneKit uses to calculate transparency for the material.
- [enum SCNTransparencyMode](../scntransparencymode.md)
  The modes SceneKit uses to calculate the opacity of pixels rendered with a material, used by the [`transparencyMode`](./transparencymode.md) property.
- [var blendMode: SCNBlendMode](./blendmode.md)
  The mode that determines how pixel colors rendered using this material blend with other pixel colors in the rendering target.
- [enum SCNBlendMode](../scnblendmode.md)
  Modes that describe how SceneKit blends source colors rendered using a material with destination colors already in a rendering target, used by the [`blendMode`](./blendmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/transparency)*