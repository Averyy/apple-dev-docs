# ModelDebugOptionsComponent.VisualizationMode.lightingDiffuse

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

A mode that displays the intensity of indirect light hitting the entity as its surface color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
case lightingDiffuse
```

## Discussion

Add a [`ModelDebugOptionsComponent`](../../modeldebugoptionscomponent.md) with a visualization mode of `lightingDiffuse` to an entity to tell RealityKit to draw the intensity of indirect, ambient lighting falling on the entity as its surface color. RealityKit represents the intensity of indirect light as a grayscale value from black (`0.0`) to white (`1.0`).

RealityKit calculates diffuse lighting for entities with a [`SimpleMaterial`](../../simplematerial.md) and for entities imported from a USDZ file. For other entities, this option has no effect.

Here’s how to enable roughness visualization for an entity:

```swift
if let television = try? await ModelEntity(named: "tv_retro") {
    let component = ModelDebugOptionsComponent(visualizationMode: .lightingDiffuse)
    television.components.set(component)
}
```

| [`ModelDebugOptionsComponent.VisualizationMode.none`](./none.md) | `lightingDiffuse` |
| --- | --- |
| ![A screenshot of a virtual TV in a visionOS app. The TV is an old-fashioned television displaying a multicolored test pattern. It is drawn with shadows and highlights to appear as realistic as possible.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/ModelDebugOptionsComponent-VisualizationMode-enum-none.jpg) | ![A screenshot of a virtual TV in a visionOS app. The TV is using a lighting diffuse visualization, appearing in shades of gray, which is a representation of the amount of indirect light falling on the TV at each point.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/ModelDebugOptionsComponent-VisualizationMode-enum-lightingDiffuse.jpg) |

## See Also

### Visualization modes
- [ModelDebugOptionsComponent.VisualizationMode.none](./none.md)
  A mode that doesn’t display a visualization.
- [ModelDebugOptionsComponent.VisualizationMode.normal](./normal.md)
  A mode that displays the normal vectors as a color.
- [ModelDebugOptionsComponent.VisualizationMode.tangent](./tangent.md)
  A mode that displays the surface tangent vectors as a color.
- [ModelDebugOptionsComponent.VisualizationMode.bitangent](./bitangent.md)
  A mode that displays the surface bitangent vectors as a color.
- [ModelDebugOptionsComponent.VisualizationMode.baseColor](./basecolor.md)
  A mode that displays the entity’s base color with no lighting or material properties applied.
- [ModelDebugOptionsComponent.VisualizationMode.textureCoordinates](./texturecoordinates.md)
  A mode that displays the texture coordinates as a color.
- [ModelDebugOptionsComponent.VisualizationMode.finalColor](./finalcolor.md)
  A mode that displays the entity’s calculated color, ignoring transparency.
- [ModelDebugOptionsComponent.VisualizationMode.finalAlpha](./finalalpha.md)
  A mode that displays the entity’s calculated transparency as its surface color.
- [ModelDebugOptionsComponent.VisualizationMode.roughness](./roughness.md)
  A mode that displays the shininess of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.metallic](./metallic.md)
  A mode that displays the reflectiveness of an entity as its surface color.
- [ModelDebugOptionsComponent.VisualizationMode.ambientOcclusion](./ambientocclusion.md)
  A mode that displays the calculated ambient occlusion value as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.specular](./specular.md)
  A mode that displays en entity’s shininess as its surface color.
- [ModelDebugOptionsComponent.VisualizationMode.emissive](./emissive.md)
  A mode that displays the emissive channel of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.clearcoat](./clearcoat.md)
  A mode that displays the clearcoat channel of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.clearcoatNormal](./clearcoatnormal.md)
  A mode that displays the clearcoat normal of a material as the surface color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modeldebugoptionscomponent/visualizationmode-swift.enum/lightingdiffuse)*