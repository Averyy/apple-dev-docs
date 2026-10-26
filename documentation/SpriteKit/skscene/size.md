# size

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The dimensions of the scene, in points.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var size: CGSize { get set }
```

```objc
@property (nonatomic) CGSize size;
```

#### Discussion

When a scene is first initialized, its size property is configured by the designated initializer. The size of the scene specifies the size of the visible portion of the scene in points. This is only used to specify the visible portion of the scene. Nodes in the tree can be positioned outside of this area; those nodes are still processed by the scene, but are ignored by the renderer.

When a scene is presented, the [`size`](./size.md) and [`anchorPoint`](./anchorpoint.md) properties determine the portion of the scene’s coordinate space that is visible in the view.

If you set the [`size`](./size.md) property to a new value, the scene’s [`didChangeSize(_:)`](./didchangesize%28_%29.md) method is called. This property can also change if the [`scaleMode`](./scalemode.md) property is set to [`SKSceneScaleMode.resizeFill`](../skscenescalemode/resizefill.md) and the presenting view is resized. After the scene’s size changes, future updates are rendered immediately at the new size.

## See Also

### Creating a Scene Programmatically
- [init(size: CGSize)](./init%28size%29.md)
  Initializes a new scene object.
- [+ sceneWithSize:](./scenewithsize_.md)
  Creates and returns a new scene object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/size)*