# automaticallyUpdatesLighting

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether ARKit creates and updates SceneKit lights in the view’s scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var automaticallyUpdatesLighting: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL automaticallyUpdatesLighting;
```

## Discussion

If this value is [`true`](../../Swift/true.md) (the default), the view automatically creates one or more [`SCNLight`](../../SceneKit/scnlight.md) objects, adds them to the scene, and updates their properties to reflect estimated lighting information from the camera scene. Set this value to [`false`](../../Swift/false.md) if you want to directly control all lighting in the SceneKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/automaticallyupdateslighting)*