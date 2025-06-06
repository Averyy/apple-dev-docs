# preferredFocusedView

**Framework**: UIKit  
**Kind**: property

Specifies the view that should be focused if this environment is focused.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
weak optional var preferredFocusedView: UIView? { get }
```

#### Discussion

Since [`UIView`](uiview.md) conforms to [`UIFocusEnvironment`](uifocusenvironment.md), any view returned from this property also has a preferred focused view. This creates a linked-list of views called the . When focus updates to a new view, the focus engine will actually update focus to the deepest, focusable view in that new view’s preferred focus chain. Similarly, when setting initial focus, such as at application launch, the initial focused view is found by following the preferred focus chain from the root window.

By default, [`UIView`](uiview.md) returns itself and [`UIViewController`](uiviewcontroller.md) returns its root view. Returning `self` in a focusable view indicates that view should be focused. Returning `self` in an unfocusable view causes the focus engine to pick a default preferred focused view, by finding the closest focusable subview to the top-leading corner of the screen. Returning `nil` indicates that there is no preferred focused view.

## See Also

- [var preferredFocusEnvironments: [any UIFocusEnvironment]](uifocusenvironment/preferredfocusenvironments.md)
  An array of focus environments, ordered by priority, to which this environment prefers focus to be directed during a focus update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/preferredfocusedview)*