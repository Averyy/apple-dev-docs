# UIContextMenuInteraction

**Framework**: UIKit  
**Kind**: class

An interaction object that you use to display relevant actions for your content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIContextMenuInteraction
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Overview

Use a [`UIContextMenuInteraction`](uicontextmenuinteraction.md) object to focus the user’s attention on a specific portion of your content, and to provide actions for the user to perform on that content. A context menu interaction object tracks Force Touch gestures on devices that support 3D Touch, and long-press gestures on devices that don’t support it. When the appropriate gesture occurs, this object animates your content to a new interface and displays the contextual menu that you supplied. UIKit manages all menu-related interactions and reports the selected action, if any, back to your app.

A context menu interaction object inherits from [`UIInteraction`](uiinteraction.md). After creating the object, assign an appropriate object to its [`delegate`](uicontextmenuinteraction/delegate.md) property and use the [`addInteraction(_:)`](uiview/addinteraction(_:).md) method to attach it to one of your views. The delegate object you provide must adopt the [`UIContextMenuInteractionDelegate`](uicontextmenuinteractiondelegate.md) protocol. Use the methods of that object to provide the contents of the contextual menu. Add your context menu interaction object to a view in your interface using the view’s [`addInteraction(_:)`](uiview/addinteraction(_:).md) method.

## Topics

### Creating a context menu interaction object
- [init(delegate: any UIContextMenuInteractionDelegate)](uicontextmenuinteraction/init(delegate:).md)
  Creates a context menu interaction object with the specified delegate object.
- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)
  Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
### Previewing and managing the content
- [var delegate: (any UIContextMenuInteractionDelegate)?](uicontextmenuinteraction/delegate.md)
  The object that provides the preview and contextual menu for your content and responds to interaction-related events.
- [protocol UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
  The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
### Getting the interaction’s location
- [func location(in: UIView?) -> CGPoint](uicontextmenuinteraction/location(in:).md)
  Returns the location of the user interaction in the specified view’s coordinate system.
### Getting the menu appearance
- [var menuAppearance: UIContextMenuInteraction.appearance](uicontextmenuinteraction/menuappearance.md)
  The appearance of the context menu.
- [UIContextMenuInteraction.appearance](uicontextmenuinteraction/appearance.md)
  Constants that describe the appearance of the menu.
### Managing menu interactions
- [func dismissMenu()](uicontextmenuinteraction/dismissmenu.md)
  Dismisses the context menu.
- [func updateVisibleMenu((UIMenu) -> UIMenu)](uicontextmenuinteraction/updatevisiblemenu(_:).md)
  Updates the currently visible menu.

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
- [UIInteraction](uiinteraction.md)

## See Also

- [class UIContextMenuSystem](uicontextmenusystem.md)
  The context menu system.
- [protocol UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
  The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
- [class UITargetedPreview](uitargetedpreview.md)
  An object describing the view to use during preview-related animations.
- [class UIPreviewTarget](uipreviewtarget.md)
  An object that specifies the container view to use for animations.
- [class UIPreviewParameters](uipreviewparameters.md)
  Additional parameters to use when animating a preview interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction)*