# animate(with:changes:completion:)

**Framework**: AppKit  
**Kind**: method

Animates changes to one or more views using the specified SwiftUI animation.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static func animate(with animation: Animation, changes: () -> Void, completion: (() -> Void)? = nil)
```

#### Discussion

Use this method to leverage SwiftUI animations from AppKit code, creating a more consistent animation experience if your app incorporates code from both frameworks.

For more information, read [`Unifying your app’s animations`](https://developer.apple.com/documentation/SwiftUI/Unifying-your-app-s-animations).

> **Note**: When a SwiftUI animation is used for animating AppKit’s [`NSAnimatablePropertyContainer`](nsanimatablepropertycontainer.md), the animations are run in-process, and are not backed by CAAnimations in the render server.

When a SwiftUI animation is used for animating AppKit’s [`NSAnimatablePropertyContainer`](nsanimatablepropertycontainer.md), the animations are run in-process, and are not backed by CAAnimations in the render server.

## Parameters

- `animation`: The animation to use for the changes.
- `changes`: A closure that contains the changes to animate.
- `completion`: A closure to execute after the animation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationcontext/animate(with:changes:completion:))*