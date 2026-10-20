# scene

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The scene to be displayed.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var scene: SCNScene? { get set }
```

```objc
@property (nonatomic, retain, nullable) SCNScene * scene;
```

#### Discussion

Setting a new scene immediately replaces whatever scene the renderer was previously displaying. To display a transition between scenes, use the [`present(_:with:incomingPointOfView:completionHandler:)`](./present%28_,with,incomingpointofview,completionhandler%29.md) method.

## See Also

### Presenting a Scene
- [func present(SCNScene, with: SKTransition, incomingPointOfView: SCNNode?, completionHandler: (() -> Void)?)](./present%28_,with,incomingpointofview,completionhandler%29.md)
  Displays the specified scene with an animated transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/scene)*