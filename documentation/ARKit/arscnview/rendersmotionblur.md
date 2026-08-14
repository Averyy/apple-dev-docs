# rendersMotionBlur

**Framework**: ARKit  
**Kind**: property

Determines whether the view renders motion blur.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var rendersMotionBlur: Bool { get set }
```

#### Discussion

This property is enabled by default. When set, the view automatically adds motion blur to rendered content which matches the visual characteristics of the motion blur ARKit observes in the camera feed.

![Screenshot showing the before and after case of virtual content rendering with motion blur.](/images/com.apple.arkit/media-3231009@2x.png)

The value of this property overwrites the [`motionBlurIntensity`](https://developer.apple.com/documentation/scenekit/scncamera/motionblurintensity) of [`SCNCamera`](https://developer.apple.com/documentation/scenekit/scncamera).

## See Also

- [var rendersCameraGrain: Bool](arscnview/renderscameragrain.md)
  A flag that determines whether SceneKit applies image noise characteristics to your app’s virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/rendersmotionblur)*