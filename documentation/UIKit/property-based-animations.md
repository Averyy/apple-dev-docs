# Property-based animations

**Framework**: UIKit

Create animations by changing the properties of a view.

## Topics

### Essentials
- [class UIViewPropertyAnimator](uiviewpropertyanimator.md)
  A class that animates changes to views and allows the dynamic modification of those animations.
- [protocol UIViewAnimating](uiviewanimating.md)
  An interface for implementing custom animator objects.
### Timing curves
- [protocol UITimingCurveProvider](uitimingcurveprovider.md)
  An interface for providing the timing information needed to perform animations.
- [class UISpringTimingParameters](uispringtimingparameters.md)
  The timing information for animations that mimics the behavior of a spring.
- [class UICubicTimingParameters](uicubictimingparameters.md)
  The timing information for animations in the form of a cubic Bézier curve.
### In-progress animations
- [protocol UIViewImplicitlyAnimating](uiviewimplicitlyanimating.md)
  An interface for modifying an animation while it’s running.

## See Also

- [View controller transitions](view-controller-transitions.md)
  Define custom transitions from one view controller to another.
- [Unifying your app’s animations](../swiftui/unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [Optimizing iPhone and iPad apps to support ProMotion displays](../quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md)
  Improve your app’s visual appearance and save power by requesting preferred refresh rates and synchronizing your animations with the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/property-based-animations)*