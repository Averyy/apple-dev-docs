# SKSceneScaleMode

**Framework**: SpriteKit  
**Kind**: enum

The modes that determine how the scene’s area is mapped to the view that presents it.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SKSceneScaleMode
```

## Topics

### Constants
- [SKSceneScaleMode.fill](skscenescalemode/fill.md)
  Each axis of the scene is scaled independently so that each axis in the scene exactly maps to the length of that axis in the view.
- [SKSceneScaleMode.aspectFill](skscenescalemode/aspectfill.md)
  The scaling factor of each dimension is calculated and the larger of the two is chosen. Each axis of the scene is scaled by the same scaling factor. This guarantees that the entire area of the view is filled but may cause parts of the scene to be cropped.
- [SKSceneScaleMode.aspectFit](skscenescalemode/aspectfit.md)
  The scaling factor of each dimension is calculated and the smaller of the two is chosen. Each axis of the scene is scaled by the same scaling factor. This guarantees that the entire scene is visible but may require letterboxing in the view.
- [SKSceneScaleMode.resizeFill](skscenescalemode/resizefill.md)
  The scene is not scaled to match the view. Instead, the scene is automatically resized so that its dimensions always match those of the view.
### Initializers
- [init?(rawValue: Int)](skscenescalemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Scaling a Scene’s Content to Fit the View](scaling-a-scene-s-content-to-fit-the-view.md)
  Configure the scale mode to determine how a scene is sized to fit its view.
- [var scaleMode: SKSceneScaleMode](skscene/scalemode.md)
  A setting that defines how the scene is mapped to the view that presents it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscenescalemode)*