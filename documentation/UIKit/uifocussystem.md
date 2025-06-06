# UIFocusSystem

**Framework**: UIKit  
**Kind**: class

Queries and reevaluates the currently focused item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIFocusSystem
```

#### Overview

Use a [`UIFocusSystem`](uifocussystem.md) object to obtain the focus-related state for the objects of your app. You can get state information for your app’s views, view controllers, windows, and other objects that adopt the [`UIFocusEnvironment`](uifocusenvironment.md) protocol. The [`UIFocusSystem`](uifocussystem.md) object lists the currently focused item, if any, for a window or view hierarchy. You can use it to force the system to update the focus state, and you can register custom sounds to be played during focus changes.

## Topics

### Getting a focus system object
- [init?(for: any UIFocusEnvironment)](uifocussystem/init(for:).md)
  Retrieves a focus system object that contains the state information for the specified object.
- [class func focusSystem(for: any UIFocusEnvironment) -> UIFocusSystem?](uifocussystem/focussystem(for:).md)
  Retrieves the focus system for the specified environment.
### Getting the currently focused item
- [var focusedItem: (any UIFocusItem)?](uifocussystem/focuseditem.md)
  The item that’s currently focused.
### Managing focus updates
- [func requestFocusUpdate(to: any UIFocusEnvironment)](uifocussystem/requestfocusupdate(to:).md)
  Submits a request to update the focus state of the specified object.
- [func updateFocusIfNeeded()](uifocussystem/updatefocusifneeded.md)
  Forces the system to act on a pending focus update for the current environment.
### Registering custom sounds
- [class func register(URL, forSoundIdentifier: UIFocusSoundIdentifier)](uifocussystem/register(_:forsoundidentifier:).md)
  Registers the specified sound file with the focus engine.
### Responding to focus-related keys and notifications
- [class let animationCoordinatorUserInfoKey: String](uifocussystem/animationcoordinatoruserinfokey.md)
  Updates the animation coordinator.
- [class let didUpdateNotification: NSNotification.Name](uifocussystem/didupdatenotification.md)
  The focus for the UI has been updated.
- [class let focusUpdateContextUserInfoKey: String](uifocussystem/focusupdatecontextuserinfokey.md)
  Updates the context key.
- [class let movementDidFailNotification: NSNotification.Name](uifocussystem/movementdidfailnotification.md)
  The focus failed to move to another item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [struct UIFocusGroupPriority](uifocusgrouppriority.md)
  The importance of an item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussystem)*