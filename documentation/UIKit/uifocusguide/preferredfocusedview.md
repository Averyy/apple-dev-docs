# preferredFocusedView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view that the focus will be redirected to if this guide is focused.

**Availability**:
- iOS 9.0+ - Deprecated in 10.0
- iPadOS 9.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 10.0

> **Deprecated**: Use [`preferredFocusEnvironments`](./preferredfocusenvironments.md) instead.

## Declaration

```swift
weak var preferredFocusedView: UIView? { get set }
```

```objc
@property (nonatomic, weak, nullable) UIView * preferredFocusedView;
```

#### Discussion

If the guide is focused, it indirects the focus to this view. This view, or at least one view along its [`preferredFocusedView`](./preferredfocusedview.md) chain, must be focusable in order for the guide to be focusable. Otherwise, it’s effectively disabled.

## See Also

### Enabling focus
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the guide is focusable.
- [var preferredFocusEnvironments: [any UIFocusEnvironment]!](./preferredfocusenvironments.md)
  An array of focus environments to which the guide directs focus, ordered by priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusguide/preferredfocusedview)*