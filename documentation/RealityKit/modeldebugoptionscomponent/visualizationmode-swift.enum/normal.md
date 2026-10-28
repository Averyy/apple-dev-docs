# ModelDebugOptionsComponent.VisualizationMode.normal

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

A mode that displays the normal vectors as a color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
case normal
```

## Discussion

Add a [`ModelDebugOptionsComponent`](../../modeldebugoptionscomponent.md) with a visualization mode of `normal` to an entity to tell RealityKit to draw that entity’s *surface normal vectors* as its surface color. A normal vector is an imaginary line perpendicular to the surface of the object at a specific point. RealityKit draws a normal vector by using its `X`, `Y`, and `Z` values as the `R`, `G`, and `B` components of the color.

RealityKit calculates normals for entities with a [`VideoMaterial`](../../videomaterial.md), [`UnlitMaterial`](../../unlitmaterial.md), or [`SimpleMaterial`](../../simplematerial.md) as well as for entities imported from a USDZ file. If an entity doesn’t fall within those parameters, this option has no effect on the rendering.

Here’s how to enable surface normal visualization for an entity:

```swift
if let television = try? await ModelEntity(named: "tv_retro") {
    let component = ModelDebugOptionsComponent(visualizationMode: .normal)
    television.components.set(component)
}
```

| [`ModelDebugOptionsComponent.VisualizationMode.none`](./none.md) | `normal` |
| --- | --- |
| ![A screenshot of a virtual TV in a visionOS app. The TV is an old-fashioned television displaying a multicolored test pattern. It is drawn with shadows and highlights to appear as realistic as possible.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/ModelDebugOptionsComponent-VisualizationMode-enum-none.jpg) | ![A screenshot of a virtual TV in a visionOS app. The TV is using a normal visualization, appearing in shades of blue, green, and purple, which is a graphical representation of the calculated normal vector at each point on the TV’s surface.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/ModelDebugOptionsComponent-VisualizationMode-enum-normal.jpg) |

## See Also

### Visualization modes
- [ModelDebugOptionsComponent.VisualizationMode.none](./none.md)
  A mode that doesn’t display a visualization.
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
- [ModelDebugOptionsComponent.VisualizationMode.clearcoatRoughness](./clearcoatroughness.md)
  A mode that displays the clearcoat roughness channel of a material as the surface color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modeldebugoptionscomponent/visualizationmode-swift.enum/normal)*