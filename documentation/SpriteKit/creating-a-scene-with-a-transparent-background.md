# Creating a Scene with a Transparent Background

**Framework**: SpriteKit

Set a transparent background color to show the content of the views below.

#### Overview

To overlay content rendered with SpriteKit on top of another view, follow these steps:

1. Set the scene’s [`backgroundColor`](skscene/backgroundcolor.md) to clear.
2. Enable [`allowsTransparency`](skview/allowstransparency.md) on the view.
3. Set the view’s [`backgroundColor`](https://developer.apple.com/documentation/UIKit/UIView/backgroundColor) to `clear`.

## See Also

- [var view: SKView?](skscene/view.md)
  The view that is currently presenting the scene.
- [var backgroundColor: UIColor](skscene/backgroundcolor.md)
  The background color of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/creating-a-scene-with-a-transparent-background)*