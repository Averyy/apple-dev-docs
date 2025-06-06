# view

**Framework**: SpriteKit  
**Kind**: property

The view that is currently presenting the scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
weak var view: SKView? { get }
```

#### Discussion

To present a scene, you call the [`presentScene(_:)`](skview/presentscene(_:).md) method or [`presentScene(_:transition:)`](skview/presentscene(_:transition:).md) method on the [`SKView`](skview.md) class. If the scene is not currently presented, this property holds `nil`.

## See Also

- [Creating a Scene with a Transparent Background](creating-a-scene-with-a-transparent-background.md)
  Set a transparent background color to show the content of the views below.
- [var backgroundColor: UIColor](skscene/backgroundcolor.md)
  The background color of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/view)*