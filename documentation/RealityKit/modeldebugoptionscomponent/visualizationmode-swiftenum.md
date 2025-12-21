# ModelDebugOptionsComponent.VisualizationMode

**Framework**: RealityKit  
**Kind**: enum

A mode that specifies the portion of the rendering process to isolate and display for debugging.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
enum VisualizationMode
```

## Topics

### Visualization modes
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
- [ModelDebugOptionsComponent.VisualizationMode.clearcoat](modeldebugoptionscomponent/visualizationmode-swift.enum/clearcoat.md)
  A mode that displays the clearcoat channel of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.clearcoatRoughness](modeldebugoptionscomponent/visualizationmode-swift.enum/clearcoatroughness.md)
  A mode that displays the clearcoat roughness channel of a material as the surface color.
- [ModelDebugOptionsComponent.VisualizationMode.lightingDiffuse](modeldebugoptionscomponent/visualizationmode-swift.enum/lightingdiffuse.md)
  A mode that displays the intensity of indirect light hitting the entity as its surface color.
- [ModelDebugOptionsComponent.VisualizationMode.lightingSpecular](modeldebugoptionscomponent/visualizationmode-swift.enum/lightingspecular.md)
  A mode that displays the intensity of direct light hitting the entity as its surface color.
### Enumeration Cases
- [ModelDebugOptionsComponent.VisualizationMode.clearcoatNormal](modeldebugoptionscomponent/visualizationmode-swift.enum/clearcoatnormal.md)
  A mode that displays the clearcoat normal of a material as the surface color.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var visualizationMode: ModelDebugOptionsComponent.VisualizationMode](modeldebugoptionscomponent/visualizationmode-swift.property.md)
  The part of the rendering process to display as the entity’s surface texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modeldebugoptionscomponent/visualizationmode-swift.enum)*