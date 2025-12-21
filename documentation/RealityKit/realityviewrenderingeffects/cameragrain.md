# cameraGrain

**Framework**: RealityKit  
**Kind**: property

Enables or disables an image noise effect for virtual content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
var cameraGrain: RealityViewRenderingEffectMode
```

#### Discussion

Images from a camera may contain a small amount of noise, called , that increases as the available light decreases. Virtual objects rendered without noise and placed into an otherwise grainy image look out of place. You can use RealityKit to add noise to the rendered output to match noise in the camera feed.

| Without camera grain | With camera grain |
| --- | --- |
| ![A screenshot of a scene with a blue sphere on a white surface. The white surface has grain, but the blue sphere does not, which makes the sphere appear out of place.](https://docs-assets.developer.apple.com/published/1f352b25e2cd3cc5669f56a96d80ea4b/ARView-RenderOptions-swift-struct-disableCameraGrain-without.jpg) | ![A screenshot of a scene with a blue sphere on a white surface. The white surface and the sphere both have gain, which makes the sphere better blend into the surroundings.](https://docs-assets.developer.apple.com/published/02fb553ab4017889f128a431dd0ecd17/ARView-RenderOptions-swift-struct-disableCameraGrain-with.jpg) |

Applying this effect involves a low, constant GPU cost. To enable or disable camera grain, set the `cameraGrain` property of the view’s [`renderingEffects`](realityviewcameracontent/renderingeffects.md).

When deciding whether to use any effect, be sure to consider your app’s CPU and GPU utilization, as described in [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md).

> ❗ **Important**: This rendering effect is unavailable on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewrenderingeffects/cameragrain)*