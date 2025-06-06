# automaticallyUpdatesLighting

**Framework**: ARKit  
**Kind**: property

A Boolean value that specifies whether ARKit creates and updates SceneKit lights in the view’s scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var automaticallyUpdatesLighting: Bool { get set }
```

#### Discussion

If this value is [`true`](https://developer.apple.com/documentation/swift/true) (the default), the view automatically creates one or more [`SCNLight`](https://developer.apple.com/documentation/SceneKit/SCNLight) objects, adds them to the scene, and updates their properties to reflect estimated lighting information from the camera scene. Set this value to [`false`](https://developer.apple.com/documentation/swift/false) if you want to directly control all lighting in the SceneKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnview/automaticallyupdateslighting)*