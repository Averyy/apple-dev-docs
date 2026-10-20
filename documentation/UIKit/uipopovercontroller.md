# UIPopoverController

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that manages the presentation of content in a popover.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: In iOS 9 and later, a popover is implemented as a [`UIViewController`](./uiviewcontroller.md) presentation. To create a popover, [`UIPopoverPresentationController`](./uipopoverpresentationcontroller.md) and specify the [`UIModalPresentationStyle.popover`](./uimodalpresentationstyle/popover.md) style.

## Declaration

```swift
@MainActor
class UIPopoverController
```

```objc
@interface UIPopoverController : NSObject
```

#### Overview

The `UIPopoverController` class is used to manage the presentation of content in a popover. You use popovers to present information temporarily. The popover content is layered on top of your existing content and the background is dimmed automatically. The popover remains visible until the user taps outside of the popover window or you explicitly dismiss it. Popover controllers are for use exclusively on iPad devices. Attempting to create one on other devices results in an exception.

To display a popover, create an instance of this class and present it using one of the appropriate methods. When initializing an instance of this class, you must specify the view controller that provides the content for the popover. Popovers normally derive their size from the view controller they present. However, you can change the size of the popover by modifying the value in the [`contentSize`](./uipopovercontroller/contentsize.md) property or by calling the [`setContentSize(_:animated:)`](./uipopovercontroller/setcontentsize%28_,animated%29.md) method. The latter approach is particularly effective if you need to animate changes to the popover’s size. The size you specify is just the preferred size for the popover’s view. The actual size may be altered to ensure that the popover fits on the screen and does not collide with the keyboard.

When displayed, taps outside of the popover window cause the popover to be dismissed automatically. To allow the user to interact with the specified views and not dismiss the popover, you can assign one or more views to the [`passthroughViews`](./uipopovercontroller/passthroughviews.md) property. Taps inside the popover window do not automatically cause the popover to be dismissed. Your view and view controller code must handle actions and events inside the popover explicitly and call the [`dismiss(animated:)`](./uipopovercontroller/dismiss%28animated%29.md) method as needed.

If the user rotates the device while a popover is visible, the popover controller hides the popover and then shows it again at the end of the rotation. The popover controller attempts to position the popover appropriately for you but you can also implement the [`popoverController(_:willRepositionPopoverTo:in:)`](./uipopovercontrollerdelegate/popovercontroller%28_,willrepositionpopoverto,in%29.md) method in the popover delegate to specify a new position.

You can assign a delegate to the popover to manage interactions with the popover and receive notifications about its dismissal. For information about the methods of the delegate object, see [`UIPopoverControllerDelegate`](./uipopovercontrollerdelegate.md).

## Topics

### Initializing the popover
- [init(contentViewController: UIViewController)](./uipopovercontroller/init%28contentviewcontroller%29.md)
  Returns an initialized popover controller object.
### Presenting and dismissing the popover
- [func present(from: CGRect, in: UIView, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](./uipopovercontroller/present%28from,in,permittedarrowdirections,animated%29.md)
  Displays the popover and anchors it to the specified location in the view.
- [func present(from: UIBarButtonItem, permittedArrowDirections: UIPopoverArrowDirection, animated: Bool)](./uipopovercontroller/present%28from,permittedarrowdirections,animated%29.md)
  Displays the popover and anchors it to the specified bar button item.
- [func dismiss(animated: Bool)](./uipopovercontroller/dismiss%28animated%29.md)
  Dismisses the popover programmatically.
### Configuring the popover content
- [var contentViewController: UIViewController](./uipopovercontroller/contentviewcontroller.md)
  The view controller responsible for the content portion of the popover.
- [func setContentView(UIViewController, animated: Bool)](./uipopovercontroller/setcontentview%28_,animated%29.md)
  Sets the view controller responsible for the content portion of the popover.
- [var contentSize: CGSize](./uipopovercontroller/contentsize.md)
  The size of the popover’s content view.
- [func setContentSize(CGSize, animated: Bool)](./uipopovercontroller/setcontentsize%28_,animated%29.md)
  Changes the size of the popover’s content view.
- [var passthroughViews: [UIView]?](./uipopovercontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.
### Getting the popover attributes
- [var isPopoverVisible: Bool](./uipopovercontroller/ispopovervisible.md)
  A Boolean value indicating whether the popover is currently visible.
- [var arrowDirection: UIPopoverArrowDirection](./uipopovercontroller/arrowdirection.md)
  The direction of the popover’s arrow.
### Accessing the delegate
- [var delegate: (any UIPopoverControllerDelegate)?](./uipopovercontroller/delegate.md)
  The delegate you want to receive popover controller messages.
### Customizing the popover appearance
- [var layoutMargins: UIEdgeInsets](./uipopovercontroller/layoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundViewClass: AnyClass?](./uipopovercontroller/backgroundviewclass.md)
  The class to use for displaying the popover background content.
- [var backgroundColor: UIColor?](./uipopovercontroller/backgroundcolor.md)
  The color of the popover’s backdrop view.
### Constants
- [struct UIPopoverArrowDirection](./uipopoverarrowdirection.md)
  Constants for specifying the direction of the popover arrow.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UIAppearanceContainer](./uiappearancecontainer.md)

## See Also

### Deprecated classes
- [class UIActionSheet](./uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
- [class UIAlertView](./uialertview.md)
  A view that displays an alert message.
- [class UIDocumentMenuViewController](./uidocumentmenuviewcontroller.md)
  A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add.
- [class UILocalNotification](./uilocalnotification.md)
  A notification that an app can schedule for presentation at a specific date and time.
- [class UIMenuController](./uimenucontroller.md)
  The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands.
- [class UIMenuItem](./uimenuitem.md)
  A custom item in the editing menu managed by the menu controller.
- [class UIMutableUserNotificationAction](./uimutableusernotificationaction.md)
  A modifiable version of the user notification action class.
- [class UIMutableUserNotificationCategory](./uimutableusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.
- [class UIPreviewAction](./uipreviewaction.md)
  A preview action, or *peek quick action*, that displays below a peek when a user swipes the peek upward.
- [class UIPreviewActionGroup](./uipreviewactiongroup.md)
  A group of one or more child quick actions, each an instance of the preview action class.
- [class UISearchDisplayController](./uisearchdisplaycontroller.md)
  An object that manages the display of a search bar, along with a table view that displays search results.
- [class UIStoryboardPopoverSegue](./uistoryboardpopoversegue.md)
  A specific type of segue for presenting content in a popover.
- [class UIWebView](./uiwebview.md)
  A view that embeds web content in your app.
- [class UIUserNotificationAction](./uiusernotificationaction.md)
  A custom action that your app can perform in response to a remote or local notification.
- [class UIUserNotificationCategory](./uiusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller)*