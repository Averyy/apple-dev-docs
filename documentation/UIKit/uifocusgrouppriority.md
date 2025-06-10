# UIFocusGroupPriority

**Framework**: UIKit  
**Kind**: struct

The importance of an item within a focus group, used by the focus system to determine the group’s primary item.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct UIFocusGroupPriority
```

## Topics

### Constants
- [static let ignored: UIFocusGroupPriority](uifocusgrouppriority/ignored.md)
  The lowest focus group priority, assigned by default.
- [static let previouslyFocused: UIFocusGroupPriority](uifocusgrouppriority/previouslyfocused.md)
  The focus group priority of a previously focused item.
- [static let prioritized: UIFocusGroupPriority](uifocusgrouppriority/prioritized.md)
  The focus group priority that indicates an item is more important than others.
- [static let currentlyFocused: UIFocusGroupPriority](uifocusgrouppriority/currentlyfocused.md)
  The focus group priority of the currently focused item, the highest possible priority.
### Initializing a focus group priority
- [init(Int)](uifocusgrouppriority/init(_:).md)
  Creates a focus group priority with the specified value.
- [init(rawValue: Int)](uifocusgrouppriority/init(rawvalue:).md)
  Creates a focus group priority with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md)
  Design and implement intuitive control schemes for menus and interactive user interface layouts.
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md)
  Create intuitive and easily manipulated user-interactive controls for your tvOS app.
- [protocol UIFocusEnvironment](uifocusenvironment.md)
  A set of methods that define the focus behavior for a branch of the view hierarchy.
- [class UIFocusSystem](uifocussystem.md)
  Queries and reevaluates the currently focused item.
- [class UIFocusUpdateContext](uifocusupdatecontext.md)
  An object that provides information relevant to a specific focus update from one view to another.
- [protocol UIFocusItem](uifocusitem.md)
  An object that can become focused.
- [class UIFocusMovementHint](uifocusmovementhint.md)
  Provides movement hint information for the focused item.
- [protocol UIFocusItemContainer](uifocusitemcontainer.md)
  The container responsible for providing geometric context to focus items within a given focus environment.
- [protocol UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md)
  A type of focus item container that supports automatic scrolling of focusable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusgrouppriority)*