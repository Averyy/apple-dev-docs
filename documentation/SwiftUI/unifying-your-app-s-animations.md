# Unifying your app’s animations

**Framework**: SwiftUI

Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.

#### Overview

Many apps use a combination of SwiftUI, UIKit, and AppKit to build and animate their interfaces. In iOS 18 and later, you can use SwiftUI animations in UIKit and AppKit. SwiftUI provides a wide range of standard as well as custom animation types.

![A conceptual illustration of a disclosure indicator, shown animating frame by frame from its collapsed position to its expanded position.](https://docs-assets.developer.apple.com/published/70aba8e027da1b7fdcabec2b06e97de9/Unifying-your-app-s-animations%402x.png)

SwiftUI, UIKit, and AppKit use different underlying implementations for animation. Apps that use multiple frameworks for animation might encounter certain issues, such as syncing animation timing or other inconsistencies, that can be difficult to troubleshoot and lead to a suboptimal user experience. Use SwiftUI animations to animate UI across all of these frameworks to create a more consistent and seamless experience on every platform.

##### Create a Swiftui Animation

To create a SwiftUI animation in UIKit or AppKit, import SwiftUI and create a SwiftUI [`Animation`](animation.md). Then, pass that animation as a parameter into the [`animate(with:changes:completion:)`](https://developer.apple.com/documentation/UIKit/UIView/animate(with:changes:completion:)) class method on `UIView`, or the [`animate(with:changes:completion:)`](https://developer.apple.com/documentation/AppKit/NSAnimationContext/animate(with:changes:completion:)) class method on `NSAnimationContext`. The following examples compare how you can create a basic spring animation using a SwiftUI [`Animation`](animation.md) type across SwiftUI, UIKit, and AppKit.

##### Use Completion Handlers with Swiftui Animations

You can provide an optional completion handler to these animation methods, which the system calls automatically after the animations complete. The following examples show a completion handler that changes the background color of the view to indicate when the animation completes.

##### Retarget a Swiftui Animation

Similar to animations in SwiftUI views, you can smoothly retarget the animations you perform using the [`animate(with:changes:completion:)`](https://developer.apple.com/documentation/UIKit/UIView/animate(with:changes:completion:)) class method on `UIView` or the [`animate(with:changes:completion:)`](https://developer.apple.com/documentation/AppKit/NSAnimationContext/animate(with:changes:completion:)) class method on `NSAnimationContext`. Retargeting a SwiftUI animation uses the velocity from the previous animations to carry the animation forward with continuous velocity, creating a fluid animation experience. The following examples show retargeting an in-progress animation.

##### Troubleshoot Animations

Syncing animations across frameworks can surface differing behavior across implementations. Keep these tips in mind when you troubleshoot animations in your app:

- SwiftUI animations run on a background thread in your app’s process.
- SwiftUI animations don’t have a backing [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation), which differentiates them from [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) animations.
- SwiftUI animations aren’t compatible with [`UIViewPropertyAnimator`](https://developer.apple.com/documentation/UIKit/UIViewPropertyAnimator) or `UIView` keyframe animations.

For more information about providing a great animation experience in your app, see [`Enhance your UI animations and transitions`](https://developer.apple.comhttps://developer.apple.com/wwdc24/10145/).

## See Also

- [struct Animation](animation.md)
  The way a view changes over time to create a smooth visual transition from one state to another.
- [func withAnimation<Result>(Animation?, () throws -> Result) rethrows -> Result](withanimation(_:_:).md)
  Returns the result of recomputing the view’s body with the provided animation.
- [@MainActor @preconcurrency static func animate(with animation: Animation = Animation.default, changes: () -> Void, completion: (() -> Void)? = nil)](../UIKit/UIView/animate(with:changes:completion:).md)
  Animates changes to one or more views using the specified SwiftUI animation.
- [static func animate(with animation: Animation, changes: () -> Void, completion: (() -> Void)? = nil)](../AppKit/NSAnimationContext/animate(with:changes:completion:).md)
  Animates changes to one or more views using the specified SwiftUI animation.
- [class NSHostingController](nshostingcontroller.md)
  An AppKit view controller that hosts SwiftUI view hierarchy.
- [class NSHostingView](nshostingview.md)
  An AppKit view that hosts a SwiftUI view hierarchy.
- [class NSHostingMenu](nshostingmenu.md)
  An AppKit menu with menu items that are defined by a SwiftUI View.
- [struct NSHostingSizingOptions](nshostingsizingoptions.md)
  Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [struct NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md)
  Options for how hosting views and controllers manage aspects of the associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/unifying-your-app-s-animations)*