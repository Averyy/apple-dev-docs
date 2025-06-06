# rendersCameraGrain

**Framework**: ARKit  
**Kind**: property

A flag that determines whether SceneKit applies image noise characteristics to your app’s virtual content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var rendersCameraGrain: Bool { get set }
```

#### Discussion

Enabled by default. When set, SceneKit adds a camera grain effect to your app’s virtual content that matches the image noise characteristics ARKit observes in the camera feed.

![Screenshot showing the before and after cases of applying image noise to an app’s virtual content.](https://docs-assets.developer.apple.com/published/91ac97857a79016f3be51942ca95e735/media-3281981%402x.png)

## See Also

- [var rendersMotionBlur: Bool](arscnview/rendersmotionblur.md)
  Determines whether the view renders motion blur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/renderscameragrain)*