# UIFocusUpdateContext

**Framework**: UIKit  
**Kind**: class

An object that provides information relevant to a specific focus update from one view to another.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIFocusUpdateContext
```

#### Overview

Focus update context objects are ephemeral and are usually discarded after the update is finished. The `UIFocus` APIs create a single high-level software interface for controlling focus in apps that use focus-based input.

## Topics

### Locating focus direction
- [var previouslyFocusedView: UIView?](uifocusupdatecontext/previouslyfocusedview.md)
  The view that was focused before the focus update.
- [var nextFocusedView: UIView?](uifocusupdatecontext/nextfocusedview.md)
  The view that takes the focus after the focus update.
- [var focusHeading: UIFocusHeading](uifocusupdatecontext/focusheading.md)
  The heading in which the focus update is occurring.
- [struct UIFocusHeading](uifocusheading.md)
  The general type of an event.
### Getting related focus items
- [var previouslyFocusedItem: (any UIFocusItem)?](uifocusupdatecontext/previouslyfocuseditem.md)
  The item that was focused before the update.
- [var nextFocusedItem: (any UIFocusItem)?](uifocusupdatecontext/nextfocuseditem.md)
  The item to be focused after the update.
### Responding to focus-related keys and notifications
- [class let didUpdateNotification: NSNotification.Name](uifocussystem/didupdatenotification.md)
  The focus for the UI has been updated.
- [class let movementDidFailNotification: NSNotification.Name](uifocussystem/movementdidfailnotification.md)
  The focus failed to move to another item.
- [class let animationCoordinatorUserInfoKey: String](uifocussystem/animationcoordinatoruserinfokey.md)
  Updates the animation coordinator.
- [class let focusUpdateContextUserInfoKey: String](uifocussystem/focusupdatecontextuserinfokey.md)
  Updates the context key.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UICollectionViewFocusUpdateContext](uicollectionviewfocusupdatecontext.md)
- [UITableViewFocusUpdateContext](uitableviewfocusupdatecontext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

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
- [protocol UIFocusItem](uifocusitem.md)
  An object that can become focused.
- [class UIFocusMovementHint](uifocusmovementhint.md)
  Provides movement hint information for the focused item.
- [protocol UIFocusItemContainer](uifocusitemcontainer.md)
  The container responsible for providing geometric context to focus items within a given focus environment.
- [protocol UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md)
  A type of focus item container that supports automatic scrolling of focusable content.
- [struct UIFocusGroupPriority](uifocusgrouppriority.md)
  The importance of an item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusupdatecontext)*