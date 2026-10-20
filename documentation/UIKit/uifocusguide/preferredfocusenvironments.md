# preferredFocusEnvironments

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of focus environments to which the guide directs focus, ordered by priority.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var preferredFocusEnvironments: [any UIFocusEnvironment]! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSArray<id<UIFocusEnvironment>> * preferredFocusEnvironments;
```

## Mentions

- [About focus interactions for Apple TV](../about-focus-interactions-for-apple-tv.md)
- [Creating custom navigation interactions](../creating-custom-navigation-interactions.md)

#### Discussion

Setting this property to a nonempty array marks this guide’s [`layoutFrame`](../uilayoutguide/layoutframe.md) as focusable. If empty, this guide is effectively disabled.

If focused, the guide attempts to redirect focus to each environment in the array, in order, stopping when a focusable item in an environment has been found.

## See Also

### Enabling focus
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the guide is focusable.
- [var preferredFocusedView: UIView?](./preferredfocusedview.md)
  The view that the focus will be redirected to if this guide is focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusguide/preferredfocusenvironments)*