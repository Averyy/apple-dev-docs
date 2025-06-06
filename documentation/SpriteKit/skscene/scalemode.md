# scaleMode

**Framework**: SpriteKit  
**Kind**: property

A setting that defines how the scene is mapped to the view that presents it.

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
var scaleMode: SKSceneScaleMode { get set }
```

## Mentions

- [Scaling a Scene’s Content to Fit the View](scaling-a-scene-s-content-to-fit-the-view.md)

#### Discussion

It is possible for a scene’s size to differ from the size of the view it is presented in. The scale mode determines how the visible portion of the scene is mapped to the view. The possible values are listed in [`SKSceneScaleMode`](skscenescalemode.md). The default value is [`SKSceneScaleMode.fill`](skscenescalemode/fill.md).

## See Also

- [Scaling a Scene’s Content to Fit the View](scaling-a-scene-s-content-to-fit-the-view.md)
  Configure the scale mode to determine how a scene is sized to fit its view.
- [enum SKSceneScaleMode](skscenescalemode.md)
  The modes that determine how the scene’s area is mapped to the view that presents it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/scalemode)*