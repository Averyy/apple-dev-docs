# depthOfField

**Framework**: RealityKit  
**Kind**: property

Enables or disables a depth of field effect for virtual content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var depthOfField: RealityViewRenderingEffectMode
```

#### Discussion

When you set the focal point of a camera, you actually choose a range of focus rather than a point. Objects outside the range — either too close or too far away — appear out of focus, while objects inside the range appear in focus. The size of the range, known as the depth of field, depends on characteristics of the lens, the focal point, and other factors.

![An illustration of a camera with three virtual objects — each a](https://docs-assets.developer.apple.com/published/158c704e1ee7bd9b531b089b488e28b9/ARView-RenderOptions-swift-struct-disableDepthOfField-1%402x.png)

If you place a virtual object outside of the range of focus, it can appear detached from the scene in which it appears unless you blur the object to match its surroundings. In many cases, the depth of field is large enough that this doesn’t matter. But if it does matter for your app, you can enable a post-processing effect that blurs virtual objects to account for depth of field.

| Without depth of field | With depth of field |
| --- | --- |
| ![A screenshot of a scene with blue and red spheres of varying distance. The scene has no depth of field, so all objects appear in focus.](https://docs-assets.developer.apple.com/published/dd8d92beaf747a023129130f0b90ba08/ARView-RenderOptions-swift-struct-disableDepthOfField-2-without.jpg) | ![A screenshot of a scene with blue and red spheres of varying distance. The scene has depth field, so the sphere in the middle appears in focus, while the closer and further spheres appear slightly blurred.](https://docs-assets.developer.apple.com/published/47ad68e38d0b8653ae311b16de8f7fa4/ARView-RenderOptions-swift-struct-disableDepthOfField-2-with.jpg) |

Because of its computational cost, [`RealityView`](realityview.md) does not apply depth of field by default. To enable depth of field, set the `depthOfField` property of the view’s [`renderingEffects`](realityviewcameracontent/renderingeffects.md). If you do enable depth of field, be sure to check your app’s performance, as described in [`Improving the Performance of a RealityKit App`](improving-the-performance-of-a-realitykit-app.md).

> ❗ **Important**: This rendering effect is unavailable on macOS.

This rendering effect is unavailable on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewrenderingeffects/depthoffield)*