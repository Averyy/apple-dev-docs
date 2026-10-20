# UIModalTransitionStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Transition styles available when presenting view controllers.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum UIModalTransitionStyle
```

```c
enum UIModalTransitionStyle : NSInteger;
```

## Topics

### Constants
- [UIModalTransitionStyle.coverVertical](./uimodaltransitionstyle/coververtical.md)
- [UIModalTransitionStyle.flipHorizontal](./uimodaltransitionstyle/fliphorizontal.md)
- [UIModalTransitionStyle.crossDissolve](./uimodaltransitionstyle/crossdissolve.md)
- [UIModalTransitionStyle.partialCurl](./uimodaltransitionstyle/partialcurl.md)
### Initializers
- [init?(rawValue: Int)](./uimodaltransitionstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Presenting a view controller
- [func show(UIViewController, sender: Any?)](./uiviewcontroller/show%28_,sender%29.md)
  Presents a view controller in a primary context.
- [func showDetailViewController(UIViewController, sender: Any?)](./uiviewcontroller/showdetailviewcontroller%28_,sender%29.md)
  Presents a view controller in a secondary (or detail) context.
- [UIViewController.ShowDetailTargetDidChangeMessage](./uiviewcontroller/showdetailtargetdidchangemessage.md)
- [func present(UIViewController, animated: Bool, completion: (() -> Void)?)](./uiviewcontroller/present%28_,animated,completion%29.md)
  Presents a view controller modally.
- [func dismiss(animated: Bool, completion: (() -> Void)?)](./uiviewcontroller/dismiss%28animated,completion%29.md)
  Dismisses the view controller that was presented modally by the view controller.
- [var modalPresentationStyle: UIModalPresentationStyle](./uiviewcontroller/modalpresentationstyle.md)
  The presentation style for modal view controllers.
- [enum UIModalPresentationStyle](./uimodalpresentationstyle.md)
  Modal presentation styles available when presenting view controllers.
- [var modalTransitionStyle: UIModalTransitionStyle](./uiviewcontroller/modaltransitionstyle.md)
  The transition style to use when presenting the view controller.
- [var isModalInPresentation: Bool](./uiviewcontroller/ismodalinpresentation.md)
  A Boolean value indicating whether the view controller enforces a modal behavior.
- [var definesPresentationContext: Bool](./uiviewcontroller/definespresentationcontext.md)
  A Boolean value that indicates whether this view controller’s view is covered when the view controller or one of its descendants presents a view controller.
- [var providesPresentationContextTransitionStyle: Bool](./uiviewcontroller/providespresentationcontexttransitionstyle.md)
  A Boolean value that indicates whether the view controller specifies the transition style for view controllers it presents.
- [var disablesAutomaticKeyboardDismissal: Bool](./uiviewcontroller/disablesautomatickeyboarddismissal.md)
  Returns a Boolean indicating whether the current input view is dismissed automatically when changing controls.
- [class let showDetailTargetDidChangeNotification: NSNotification.Name](./uiviewcontroller/showdetailtargetdidchangenotification.md)
  Posted when a split view controller is expanded or collapsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimodaltransitionstyle)*