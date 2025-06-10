# Applying Special Effects to a Node’s Children

**Framework**: SpriteKit

Apply the Core Image suite of filters to child nodes of an effect node.

#### Overview

In the example image below, the effect node’s children are two sprites that provide lighting information. The effect node accumulates the effects of these lights, applies a blur filter to soften the resulting image, and uses a multiply blend mode to apply this lighting to a texture.

> ❗ **Important**:  Any Core Image filter that you use must be able to produce a single output image from a single input image.

![None](https://docs-assets.developer.apple.com/published/3d38d07c6cf154b78e4a8e1ef1270a5c/media-3111373%402x.png)

Hereʼs how the scene generates this lighting effect:

1. The scene has two children. The first is a textured sprite that represents the ground. The second is an effect node to apply lighting.
2. The effect nodeʼs children are sprite nodes rendered using an additive blend mode.
3. The effect node includes a filter effect to soften the lighting.
4. The effect node uses a multiplication blend mode to apply its lighting effect to the sceneʼs framebuffer.

The following Swift code demonstrates an implementation of this technique:

```swift
let lightingNode = SKEffectNode()

let light = SKSpriteNode(texture: lightTexture)
light.blendMode = .add
...
lightingNode.addChild(light)

let blurFilter = CIFilter(name: "CIBoxBlur",
withInputParameters: ["inputRadius": 20])

lightingNode.filter = blurFilter

lightingNode.blendMode = .multiply
```

## See Also

- [var filter: CIFilter?](skeffectnode/filter.md)
  The Core Image filter to apply.
- [var shouldEnableEffects: Bool](skeffectnode/shouldenableeffects.md)
  A Boolean value that determines whether the effect node applies the filter to its children as they are drawn.
- [var shouldCenterFilter: Bool](skeffectnode/shouldcenterfilter.md)
  A Boolean value that determines whether the effect node automatically sets the filter’s image center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/applying-special-effects-to-a-node-s-children)*