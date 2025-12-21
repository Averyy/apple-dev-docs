# UIDocumentMenuViewController

**Framework**: UIKit  
**Kind**: class

A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UIDocumentMenuViewController
```

## Topics

### Creating a document menu
- [init(documentTypes: [String], in: UIDocumentPickerMode)](uidocumentmenuviewcontroller/init(documenttypes:in:).md)
  Initializes and returns a document menu to import or open the given file types.
- [init(url: URL, in: UIDocumentPickerMode)](uidocumentmenuviewcontroller/init(url:in:).md)
  Initializes and returns a document menu to export or move the given document.
- [init?(coder: NSCoder)](uidocumentmenuviewcontroller/init(coder:).md)
  Creates a document menu from data in an unarchiver.
### Getting the user-selected document picker
- [var delegate: (any UIDocumentMenuDelegate)?](uidocumentmenuviewcontroller/delegate.md)
  The document menu’s delegate.
- [protocol UIDocumentMenuDelegate](uidocumentmenudelegate.md)
  A set of methods that you must implement to track user interactions with a document menu view controller.
### Configuring a document menu
- [func addOption(withTitle: String, image: UIImage?, order: UIDocumentMenuOrder, handler: () -> Void)](uidocumentmenuviewcontroller/addoption(withtitle:image:order:handler:).md)
  Adds a custom menu item to the list of document pickers.
- [enum UIDocumentMenuOrder](uidocumentmenuorder.md)
  The insertion point for custom menu items.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIActionSheet](uiactionsheet.md)
  A view that presents a set of alternatives for how to proceed with a task.
- [class UIAlertView](uialertview.md)
  A view that displays an alert message.
- [class UILocalNotification](uilocalnotification.md)
  A notification that an app can schedule for presentation at a specific date and time.
- [class UIMenuController](uimenucontroller.md)
  The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands.
- [class UIMenuItem](uimenuitem.md)
  A custom item in the editing menu managed by the menu controller.
- [class UIMutableUserNotificationAction](uimutableusernotificationaction.md)
  A modifiable version of the user notification action class.
- [class UIMutableUserNotificationCategory](uimutableusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.
- [class UIPopoverController](uipopovercontroller.md)
  An object that manages the presentation of content in a popover.
- [class UIPreviewAction](uipreviewaction.md)
  A preview action, or , that displays below a peek when a user swipes the peek upward.
- [class UIPreviewActionGroup](uipreviewactiongroup.md)
  A group of one or more child quick actions, each an instance of the preview action class.
- [class UISearchDisplayController](uisearchdisplaycontroller.md)
  An object that manages the display of a search bar, along with a table view that displays search results.
- [class UIStoryboardPopoverSegue](uistoryboardpopoversegue.md)
  A specific type of segue for presenting content in a popover.
- [class UIWebView](uiwebview.md)
  A view that embeds web content in your app.
- [class UIUserNotificationAction](uiusernotificationaction.md)
  A custom action that your app can perform in response to a remote or local notification.
- [class UIUserNotificationCategory](uiusernotificationcategory.md)
  Information about custom actions that your app can perform in response to a local or push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller)*