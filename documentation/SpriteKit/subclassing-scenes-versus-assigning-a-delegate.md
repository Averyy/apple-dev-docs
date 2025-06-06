# Subclassing Scenes Versus Assigning a Delegate

**Framework**: SpriteKit

Use a scene delegate to share app logic across various scenes.

#### Overview

Often, your app subclasses [`SKScene`](skscene.md) to deliver gameplay. Your subclass usually:

- Lays out initial scene content
- Defines app logic that runs every frame
- Implements responder methods to handle keyboard, mouse, or touch events

An alternative pattern is to assign a [`delegate`](skview/delegate.md) that handles [`SKScene`](skscene.md) instead. For example, if you make the view controller the delegate for your scene, it can use multiple scenes that share the same [`SKSceneDelegate`](skscenedelegate.md) implementations. The view controller participates in event handling and so it can respond to user input also.

> ❗ **Important**:  On macOS, you need to set the window’s [`nextResponder`](https://developer.apple.com/documentation/AppKit/NSResponder/nextResponder) to your app’s view controller because by default, the view is the first responder to user input events.

 On macOS, you need to set the window’s [`nextResponder`](https://developer.apple.com/documentation/AppKit/NSResponder/nextResponder) to your app’s view controller because by default, the view is the first responder to user input events.

## See Also

- [var delegate: (any SKSceneDelegate)?](skscene/delegate.md)
  A delegate to be called during the animation loop.
- [protocol SKSceneDelegate](skscenedelegate.md)
  Methods that, when implemented, allow any class to participate in the SpriteKit render loop callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/subclassing-scenes-versus-assigning-a-delegate)*