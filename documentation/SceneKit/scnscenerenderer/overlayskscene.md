# overlaySKScene

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Sprite Kit scene to be rendered on top of the SceneKit content.

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
var overlaySKScene: SKScene? { get set }
```

```objc
@property (nonatomic, retain, nullable) SKScene * overlaySKScene;
```

## Discussion

Use this property to render 2D content that overlays your scene—for example, a heads-up-display for a game. The Sprite Kit scene shares the same underlying GPU resources as the SceneKit renderer, so using this property can provide much better performance than overlaying other views or layers above the view rendering your SceneKit content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/overlayskscene)*