# ModelDebugOptionsComponent.VisualizationMode.clearcoatNormal

**Framework**: RealityKit  
**Kind**: case

A mode that displays the clearcoat normal of a material as the surface color.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
case clearcoatNormal
```

#### Discussion

Adding a [`ModelDebugOptionsComponent`](modeldebugoptionscomponent.md) with a visualization mode of `clearcoatNormal` to an entity tells RealityKit to draw the world space clearcoat normal as its surface color. RealityKit draws the xyz value as a rgb color value after it has been transformed from tangent to world space.

Here’s how to enable clearcoat normal visualization for an entity:

```swift
if let television = try? await ModelEntity(named: "tv_retro") {
    let component = ModelDebugOptionsComponent(visualizationMode: .clearcoatNormal)
    television.components.set(component)
}
```

| [`ModelDebugOptionsComponent.VisualizationMode.none`](modeldebugoptionscomponent/visualizationmode-swift.enum/none.md) | `clearcoatNormal` |
| --- | --- |
| ![A screenshot of a virtual TV in a visionOS app. The TV is an old-fashioned television displaying a multicolored test pattern. It is drawn with shadows and highlights to appear as realistic as possible.](https://docs-assets.developer.apple.com/published/a57e508a6549f1c8cce08e79ea6b7ec5/ModelDebugOptionsComponent-VisualizationMode-enum-none.jpg) | ![A screenshot of a virtual TV in a visionOS app. The TV is using a clearcoat normal visualization, appearing in black. This is a graphical representation of the TV’s clearcoat normal values.](https://docs-assets.developer.apple.com/published/4e6cab4f718596d074ddd55ac9c5fb21/ModelDebugOptionsComponent-VisualizationMode-enum-clearcoatNormal.jpg) |


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modeldebugoptionscomponent/visualizationmode-swift.enum/clearcoatnormal)*