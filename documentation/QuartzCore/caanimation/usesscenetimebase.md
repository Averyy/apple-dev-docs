# usesSceneTimeBase

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

For animations attached to SceneKit objects, a Boolean value that determines whether the animation is evaluated using the scene time or the system time.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var usesSceneTimeBase: Bool { get set }
```

```objc
@property BOOL usesSceneTimeBase;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), animation timing is governed by the currentTime property of the view, layer, or custom renderer responsible for drawing the scene. The default value is [`false`](../../Swift/false.md).

To attach animations to SceneKit objects, see [`SCNAnimatable`](../../SceneKit/scnanimatable.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimation/usesscenetimebase)*