# preferredFocusedView

**Framework**: UIKit  
**Kind**: property

The view that the focus will be redirected to if this guide is focused.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
@MainActor
weak var preferredFocusedView: UIView? { get set }
```

#### Discussion

If the guide is focused, it indirects the focus to this view. This view, or at least one view along its [`preferredFocusedView`](uifocusguide/preferredfocusedview.md) chain, must be focusable in order for the guide to be focusable. Otherwise, it’s effectively disabled.

## See Also

- [var isEnabled: Bool](uifocusguide/isenabled.md)
  A Boolean value that indicates whether the guide is focusable.
- [var preferredFocusEnvironments: [any UIFocusEnvironment]!](uifocusguide/preferredfocusenvironments.md)
  An array of focus environments to which the guide directs focus, ordered by priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusguide/preferredfocusedview)*