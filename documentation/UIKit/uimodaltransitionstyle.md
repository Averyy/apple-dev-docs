# UIModalTransitionStyle

**Framework**: UIKit  
**Kind**: enum

Transition styles available when presenting view controllers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum UIModalTransitionStyle
```

## Topics

### Constants
- [UIModalTransitionStyle.coverVertical](uimodaltransitionstyle/coververtical.md)
- [UIModalTransitionStyle.flipHorizontal](uimodaltransitionstyle/fliphorizontal.md)
- [UIModalTransitionStyle.crossDissolve](uimodaltransitionstyle/crossdissolve.md)
- [UIModalTransitionStyle.partialCurl](uimodaltransitionstyle/partialcurl.md)
### Initializers
- [init?(rawValue: Int)](uimodaltransitionstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func show(UIViewController, sender: Any?)](uiviewcontroller/show(_:sender:).md)
  Presents a view controller in a primary context.
- [func showDetailViewController(UIViewController, sender: Any?)](uiviewcontroller/showdetailviewcontroller(_:sender:).md)
  Presents a view controller in a secondary (or detail) context.
- [func present(UIViewController, animated: Bool, completion: (() -> Void)?)](uiviewcontroller/present(_:animated:completion:).md)
  Presents a view controller modally.
- [func dismiss(animated: Bool, completion: (() -> Void)?)](uiviewcontroller/dismiss(animated:completion:).md)
  Dismisses the view controller that was presented modally by the view controller.
- [var modalPresentationStyle: UIModalPresentationStyle](uiviewcontroller/modalpresentationstyle.md)
  The presentation style for modal view controllers.
- [enum UIModalPresentationStyle](uimodalpresentationstyle.md)
  Modal presentation styles available when presenting view controllers.
- [var modalTransitionStyle: UIModalTransitionStyle](uiviewcontroller/modaltransitionstyle.md)
  The transition style to use when presenting the view controller.
- [var isModalInPresentation: Bool](uiviewcontroller/ismodalinpresentation.md)
  A Boolean value indicating whether the view controller enforces a modal behavior.
- [var definesPresentationContext: Bool](uiviewcontroller/definespresentationcontext.md)
  A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [var providesPresentationContextTransitionStyle: Bool](uiviewcontroller/providespresentationcontexttransitionstyle.md)
  A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [var disablesAutomaticKeyboardDismissal: Bool](uiviewcontroller/disablesautomatickeyboarddismissal.md)
  Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimodaltransitionstyle)*