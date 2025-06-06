# Focus-based navigation

**Framework**: UIKit

Navigate the interface of your UIKit app using a remote, game controller, or keyboard.

## Topics

### Focus interactions
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
- [struct UIFocusGroupPriority](uifocusgrouppriority.md)
  The importance of an item within a focus group, used by the focus system to determine the group’s primary item.
### Focus guides
- [Creating custom navigation interactions](creating-custom-navigation-interactions.md)
  Build nonstandard navigation interactions that move focus to the desired location.
- [class UIFocusGuide](uifocusguide.md)
  An object that exposes nonview areas as focusable.
### Focus debugging
- [Debugging focus issues in your app](debugging-focus-issues-in-your-app.md)
  Find errors and determine why the next focused item isn’t what you expected.
- [class UIFocusDebugger](uifocusdebugger.md)
  A runtime object for debugging focus-related interactions.
### Animations
- [class UIFocusAnimationCoordinator](uifocusanimationcoordinator.md)
  A coordinator of focus-related animations during a focus update.
### Focus effects
- [class UIFocusEffect](uifocuseffect.md)
  The base class for defining a visual focus effect.
- [class UIFocusHaloEffect](uifocushaloeffect.md)
  A visual focus effect that draws a halo around the focus item.
- [UIFocusHaloEffect.Position](uifocushaloeffect/position-swift.enum.md)
  Constants that describe positions for drawing the halo focus effect.

## See Also

- [Touches, presses, and gestures](touches-presses-and-gestures.md)
  Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Menus and shortcuts](menus-and-shortcuts.md)
  Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.
- [Drag and drop](drag-and-drop.md)
  Bring drag and drop to your app by using interaction APIs with your views.
- [Pointer interactions](pointer-interactions.md)
  Support pointer interactions in your custom controls and views.
- [Apple Pencil interactions](apple-pencil-interactions.md)
  Handle user interactions like double tap and squeeze on Apple Pencil.
- [Accessibility for UIKit](accessibility-for-uikit.md)
  Make your UIKit apps accessible to everyone who uses iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/focus-based-navigation)*