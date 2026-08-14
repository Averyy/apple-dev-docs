# ModelDebugOptionsComponent.VisualizationMode.ambientOcclusion

**Framework**: RealityKit  
**Kind**: case

A mode that displays the calculated ambient occlusion value as the surface color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
case ambientOcclusion
```

#### Discussion

Add a [`ModelDebugOptionsComponent`](modeldebugoptionscomponent.md) with a visualization mode of `ambientOcclusion` to an entity to tell RealityKit to draw the calculated ambient occlusion values as the entity’s surface color. Ambient occlusion represents the entity’s exposure to ambient light. RealityKit draws ambient occlusion values as a grayscale value from black (`0.0`) to white (`1.0`), rendering flat surface areas in white, and crevices, dents, and recessed areas in darker shades.

RealityKit calculates ambient occlusion for entities with a [`SimpleMaterial`](simplematerial.md) and for entities imported from a USDZ file. For other entities, this option has no effect.

Here’s how to enable ambient occlusion visualization for an entity:

```swift
if let television = try? await ModelEntity(named: "tv_retro") {
    let component = ModelDebugOptionsComponent(visualizationMode: .ambientOcclusion)
    television.components.set(component)
}
```

| [`ModelDebugOptionsComponent.VisualizationMode.none`](modeldebugoptionscomponent/visualizationmode-swift.enum/none.md) | `ambientOcclusion` |
| --- | --- |
| ![A screenshot of a virtual TV in a visionOS app. The TV is an old-fashioned television displaying a multicolored test pattern. It is drawn with shadows and highlights to appear as realistic as possible.](/images/com.apple.RealityKit/ModelDebugOptionsComponent-VisualizationMode-enum-none.jpg) | ![A screenshot of a virtual TV in a visionOS app. The TV is using an ambient occlusion visualization, appearing in white and gray, which is a graphical representation of the TV’s ambient occlusion values.](/images/com.apple.RealityKit/ModelDebugOptionsComponent-VisualizationMode-enum-ambientOcclusion.jpg) |

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
- [ModelDebugOptionsComponent.VisualizationMode.specular](modeldebugoptionscomponent/visualizationmode-swift.enum/specular.md)
  A mode that displays en entity’s shininess as its surface color.
- [ModelDebugOptionsComponent.VisualizationMode.emissive](modeldebugoptionscomponent/visualizationmode-swift.enum/emissive.md)
  A mode that displays the emissive channel of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.clearcoat](modeldebugoptionscomponent/visualizationmode-swift.enum/clearcoat.md)
  A mode that displays the clearcoat channel of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.clearcoatNormal](modeldebugoptionscomponent/visualizationmode-swift.enum/clearcoatnormal.md)
  A mode that displays the clearcoat normal of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.clearcoatRoughness](modeldebugoptionscomponent/visualizationmode-swift.enum/clearcoatroughness.md)
  A mode that displays the clearcoat roughness channel of a material as the surface color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modeldebugoptionscomponent/visualizationmode-swift.enum/ambientocclusion)*