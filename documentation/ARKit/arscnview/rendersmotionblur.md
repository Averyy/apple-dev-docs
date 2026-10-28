# rendersMotionBlur

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

Determines whether the view renders motion blur.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var rendersMotionBlur: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL rendersMotionBlur;
```

## Discussion

This property is enabled by default. When set, the view automatically adds motion blur to rendered content which matches the visual characteristics of the motion blur ARKit observes in the camera feed.

![Screenshot showing the before and after case of virtual content rendering with motion blur.](https://developer.apple.com/tutorials/images/com.apple.arkit/media-3231009@2x.png)

The value of this property overwrites the [`motionBlurIntensity`](../../SceneKit/scncamera/motionblurintensity.md) of [`SCNCamera`](../../SceneKit/scncamera.md).

## See Also

### Managing Rendering Effects
- [var rendersCameraGrain: Bool](./renderscameragrain.md)
  A flag that determines whether SceneKit applies image noise characteristics to your app’s virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/rendersmotionblur)*