# Adding user-focusable elements to a tvOS app

**Framework**: UIKit

Create intuitive and easily manipulated user-interactive controls for your tvOS app.

#### Overview

On Apple TV, people use a remote or game controller to navigate through interface elements like movie posters, apps, or buttons, highlighting each item as they come to it. The highlighted item is said to be  or . It appears elevated or otherwise distinct from other items. An item is considered focused when the user has highlighted it, but not selected it. The user moves focus by navigating through different UI items, which triggers a focus update.

##### Add Focusable Items to the View

In Xcode, search the Library pane for the item you want to add to your app, and drag it to your app’s storyboard. Several UIKit elements are focusable by default, including buttons ([`UIButton`](uibutton.md)), text fields ([`UITextField`](uitextfield.md)), and table cells ([`UITableViewCell`](uitableviewcell.md)). The top-left item is in focus when your app launches. (In right-to-left languages, the top-right item is initially in focus.) You don’t need to do anything to UIKit elements that are focusable by default. However, you can add SceneKit and SpriteKit nodes as focusable elements. To make a SceneKit or SpriteKit node focusable, set the [`focusBehavior`](https://developer.apple.com/documentation/SpriteKit/SKNode/focusBehavior) property of the node to `focusable`, as shown below.

```swift
node.focusBehavior = .focusable
```

##### Design Your Layout in a Grid Pattern

The easiest way to ensure that focus moves between focusable items is to arrange the items in a grid pattern. Swiping on the remote triggers the focus engine—the system that controls focus and movement—to find all of the focusable items in the direction of the swipe. The first item found then becomes the newly focused item. The following image shows the items found by the focus engine when the user swipes right, and the resulting focused item.

![Image that shows the result of swiping right on the remote.](https://docs-assets.developer.apple.com/published/40e8a8d70b354eaae5c29913389c254f/media-2923202%402x.png)

The following image shows the items found by the focus engine when the user swipes down, and the resulting focused item.

![Image that shows the result of swiping down on the remote.](https://docs-assets.developer.apple.com/published/42b84cff9a5af577e38c4344dbe5e95c/media-2923200%402x.png)

When the focus engine doesn’t find any items in the direction of the swipe, by default the focused item doesn’t change, as shown in the following image.

![Image that shows the result of swiping down with no items.](https://docs-assets.developer.apple.com/published/dd1cf54e395780106979fafdd2d05f2f/media-2923201%402x.png)

When necessary, you can change the default behavior by using [`UIFocusGuide`](uifocusguide.md) to redirect focus to other focusable items in the user interface.

## See Also

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md)
  Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md)
  Design and implement intuitive control schemes for menus and interactive user interface layouts.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/adding-user-focusable-elements-to-a-tvos-app)*