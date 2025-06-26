# UIFocusGuide

**Framework**: UIKit  
**Kind**: class

An object that exposes nonview areas as focusable.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIFocusGuide
```

## Mentions

- [Creating custom navigation interactions](creating-custom-navigation-interactions.md)
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md)

#### Overview

As a subclass of [`UILayoutGuide`](uilayoutguide.md), a focus guide is not a view and does not define a new view or participate in the view hierarchy at all, except as an Auto Layout guide. Unlike [`UILayoutGuide`](uilayoutguide.md), [`UIFocusGuide`](uifocusguide.md) represents an invisible, focusable region that can redirect focus movement to other views. The `UIFocus.h` header file, including its related classes and its protocol, creates a single high-level software interface for controlling focus in apps that use focus-based input. This programming interface also helps to control focus behavior on the screen.

## Topics

### Enabling focus
- [var isEnabled: Bool](uifocusguide/isenabled.md)
  A Boolean value that indicates whether the guide is focusable.
- [var preferredFocusEnvironments: [any UIFocusEnvironment]!](uifocusguide/preferredfocusenvironments.md)
  An array of focus environments to which the guide directs focus, ordered by priority.
- [var preferredFocusedView: UIView?](uifocusguide/preferredfocusedview.md)
  The view that the focus will be redirected to if this guide is focused.

## Relationships

### Inherits From
- [UILayoutGuide](uilayoutguide.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## See Also

- [Creating custom navigation interactions](creating-custom-navigation-interactions.md)
  Build nonstandard navigation interactions that move focus to the desired location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusguide)*