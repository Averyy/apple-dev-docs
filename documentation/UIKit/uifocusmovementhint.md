# UIFocusMovementHint

**Framework**: UIKit  
**Kind**: class

Provides movement hint information for the focused item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class UIFocusMovementHint
```

## Topics

### Moving focus
- [var movementDirection: CGVector](uifocusmovementhint/movementdirection.md)
  A vector representing how close focus is to moving to another item in the swiped direction.
### Transforming a hint
- [var interactionTransform: CATransform3D](uifocusmovementhint/interactiontransform.md)
  A 3D transform that contains the combined transformations of perspective, rotation, and translation.
- [var perspectiveTransform: CATransform3D](uifocusmovementhint/perspectivetransform.md)
  A 3D transform that represents a perspective matrix to be applied to match UIKit interaction hinting.
- [var rotation: CGVector](uifocusmovementhint/rotation.md)
  A vector to apply to a transform to match system interaction hinting.
- [var translation: CGVector](uifocusmovementhint/translation.md)
  A vector to apply to a transform to match system interaction hinting.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [protocol UIFocusItemContainer](uifocusitemcontainer.md)
  The container responsible for providing geometric context to focus items within a given focus environment.
- [protocol UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md)
  A type of focus item container that supports automatic scrolling of focusable content.
- [struct UIFocusGroupPriority](uifocusgrouppriority.md)
  The importance of an item within a focus group, used by the focus system to determine the group’s primary item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusmovementhint)*