# exposureDuration

**Framework**: ARKit  
**Kind**: property

A value you use to effect motion blur when rendering your app’s virtual content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var exposureDuration: TimeInterval { get }
```

#### Discussion

If you display an AR experience using a custom Metal renderer, use this value to determine how much motion blur to apply to your virtual content.

If [`ARSCNView`](arscnview.md) is your renderer, SceneKit automatically applies motion blur to your virtual content. For more information, see [`rendersMotionBlur`](arscnview/rendersmotionblur.md).

![Screenshot showing the before and after case of virtual content rendering with motion blur.](/images/com.apple.arkit/media-3231008@2x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/exposureduration)*