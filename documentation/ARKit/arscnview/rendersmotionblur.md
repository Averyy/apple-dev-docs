# rendersMotionBlur

**Framework**: ARKit  
**Kind**: property

Determines whether the view renders motion blur.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var rendersMotionBlur: Bool { get set }
```

#### Discussion

This property is enabled by default. When set, the view automatically adds motion blur to rendered content which matches the visual characteristics of the motion blur ARKit observes in the camera feed.

![Screenshot showing the before and after case of virtual content rendering with motion blur.](https://docs-assets.developer.apple.com/published/355e2c150e6b31f68b1f99074bfa3127/media-3231009%402x.png)

The value of this property overwrites the [`motionBlurIntensity`](https://developer.apple.com/documentation/SceneKit/SCNCamera/motionBlurIntensity) of [`SCNCamera`](https://developer.apple.com/documentation/SceneKit/SCNCamera).

## See Also

- [var rendersCameraGrain: Bool](arscnview/renderscameragrain.md)
  A flag that determines whether SceneKit applies image noise characteristics to your app’s virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/rendersmotionblur)*