# ModelDebugOptionsComponent.VisualizationMode.clearcoat

**Framework**: RealityKit  
**Kind**: case

A mode that displays the clearcoat channel of a material as the surface color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
case clearcoat
```

#### Discussion

Add a [`ModelDebugOptionsComponent`](modeldebugoptionscomponent.md) with a visualization mode of `clearcoat` to an entity to tell RealityKit to draw the entity’s clearcoat values as its surface color. A clearcoat is a way to render objects that appear to have a transparent coating or veneer, such as the surface of a car with a coat of wax or items shrinkwrapped in clear plastic. RealityKit draws clearcoat values as a grayscale value from black (`0.0`) to white (`1.0`), with black representing parts of the entity that don’t use clearcoat.

RealityKit calculates clearcoat for entities with a [`SimpleMaterial`](simplematerial.md) and for entities imported from a USDZ file. For other entities, this option has no effect.

Here’s how to enable roughness visualization for an entity:

```swift
if let television = try? await ModelEntity(named: "tv_retro") {
    let component = ModelDebugOptionsComponent(visualizationMode: .clearcoat)
    television.components.set(component)
}
```

| [`ModelDebugOptionsComponent.VisualizationMode.none`](modeldebugoptionscomponent/visualizationmode-swift.enum/none.md) | `clearcoat` |
| --- | --- |
| ![A screenshot of a virtual TV in a visionOS app. The TV is an old-fashioned television displaying a multicolored test pattern. It is drawn with shadows and highlights to appear as realistic as possible.](https://docs-assets.developer.apple.com/published/a57e508a6549f1c8cce08e79ea6b7ec5/ModelDebugOptionsComponent-VisualizationMode-enum-none.jpg) | ![A screenshot of a virtual TV in a visionOS app. The TV is using a clearcoat visualization, appearing in black. This is a graphical representation of the TV’s clearcoat values.](https://docs-assets.developer.apple.com/published/dd883998f0fb578907595c7e2835d5eb/ModelDebugOptionsComponent-VisualizationMode-enum-clearcoat.jpg) |

## See Also

- [ModelDebugOptionsComponent.VisualizationMode.none](modeldebugoptionscomponent/visualizationmode-swift.enum/none.md)
  A mode that doesn’t display a visualization.
- [ModelDebugOptionsComponent.VisualizationMode.normal](modeldebugoptionscomponent/visualizationmode-swift.enum/normal.md)
  A mode that displays the normal vectors as a color.
- [ModelDebugOptionsComponent.VisualizationMode.tangent](modeldebugoptionscomponent/visualizationmode-swift.enum/tangent.md)
  A mode that displays the surface tangent vectors as a color.
- [ModelDebugOptionsComponent.VisualizationMode.bitangent](modeldebugoptionscomponent/visualizationmode-swift.enum/bitangent.md)
  A mode that displays the surface bitangent vectors as a color.
- [ModelDebugOptionsComponent.VisualizationMode.baseColor](modeldebugoptionscomponent/visualizationmode-swift.enum/basecolor.md)
  A mode that displays the entity’s base color with no lighting or material properties applied.
- [ModelDebugOptionsComponent.VisualizationMode.textureCoordinates](modeldebugoptionscomponent/visualizationmode-swift.enum/texturecoordinates.md)
  A mode that displays the texture coordinates as a color.
- [ModelDebugOptionsComponent.VisualizationMode.finalColor](modeldebugoptionscomponent/visualizationmode-swift.enum/finalcolor.md)
  A mode that displays the entity’s calculated color, ignoring transparency.
- [ModelDebugOptionsComponent.VisualizationMode.finalAlpha](modeldebugoptionscomponent/visualizationmode-swift.enum/finalalpha.md)
  A mode that displays the entity’s calculated transparency as its surface color.
- [ModelDebugOptionsComponent.VisualizationMode.roughness](modeldebugoptionscomponent/visualizationmode-swift.enum/roughness.md)
  A mode that displays the shininess of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.metallic](modeldebugoptionscomponent/visualizationmode-swift.enum/metallic.md)
  A mode that displays the reflectiveness of an entity as its surface color.
- [ModelDebugOptionsComponent.VisualizationMode.ambientOcclusion](modeldebugoptionscomponent/visualizationmode-swift.enum/ambientocclusion.md)
  A mode that displays the calculated ambient occlusion value as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.specular](modeldebugoptionscomponent/visualizationmode-swift.enum/specular.md)
  A mode that displays en entity’s shininess as its surface color.
- [ModelDebugOptionsComponent.VisualizationMode.emissive](modeldebugoptionscomponent/visualizationmode-swift.enum/emissive.md)
  A mode that displays the emissive channel of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.clearcoatRoughness](modeldebugoptionscomponent/visualizationmode-swift.enum/clearcoatroughness.md)
  A mode that displays the clearcoat roughness channel of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.lightingDiffuse](modeldebugoptionscomponent/visualizationmode-swift.enum/lightingdiffuse.md)
  A mode that displays the intensity of indirect light hitting the entity as its surface color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modeldebugoptionscomponent/visualizationmode-swift.enum/clearcoat)*