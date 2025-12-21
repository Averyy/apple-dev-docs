# size

**Framework**: SpriteKit  
**Kind**: property

The dimensions of the scene, in points.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var size: CGSize { get set }
```

#### Discussion

When a scene is first initialized, its size property is configured by the designated initializer. The size of the scene specifies the size of the visible portion of the scene in points. This is only used to specify the visible portion of the scene. Nodes in the tree can be positioned outside of this area; those nodes are still processed by the scene, but are ignored by the renderer.

When a scene is presented, the [`size`](skscene/size.md) and [`anchorPoint`](skscene/anchorpoint.md) properties determine the portion of the scene’s coordinate space that is visible in the view.

If you set the [`size`](skscene/size.md) property to a new value, the scene’s [`didChangeSize(_:)`](skscene/didchangesize(_:).md) method is called. This property can also change if the [`scaleMode`](skscene/scalemode.md) property is set to [`SKSceneScaleMode.resizeFill`](skscenescalemode/resizefill.md) and the presenting view is resized. After the scene’s size changes, future updates are rendered immediately at the new size.

## See Also

- [init(size: CGSize)](skscene/init(size:).md)
  Initializes a new scene object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/size)*