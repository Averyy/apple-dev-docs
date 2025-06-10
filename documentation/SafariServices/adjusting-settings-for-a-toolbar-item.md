# Adjusting settings for a toolbar item

**Framework**: Safari Services

Customize a toolbar item for your Safari app extension.

#### Overview

Safari has a user-customizable toolbar that can contain a selection of buttons. A Safari app extension can provide a new toolbar item, and when the Safari app extension is in an enabled state, Safari adds that item to the toolbar by default. The user may choose to hide your toolbar item by customizing the toolbar.

![A screenshot of the Safari toolbar. It shows standard toolbar items, as well as an app extension toolbar item that looks like a lightning bolt inside a circle. ](https://docs-assets.developer.apple.com/published/c4108e139b0ba0285b01ac6b2fb411b1/media-2958181%402x.png)

Your app extension can enable or disable the toolbar item or add a badge with text to it. When the user clicks it, the toolbar item can either execute a command or display a popover. The decision of which behavior to implement occurs at design time. For more information, see [`Display a popover for a toolbar item`](adjusting-settings-for-a-toolbar-item#Display-a-popover-for-a-toolbar-item.md).

Add a toolbar item with the following steps:

1. Create an image.
2. Fill out the appropriate fields in the `Info.plist` file.
3. Add logic that executes when the user clicks the toolbar button.

To learn how to add a toolbar item, see [`Using contextual menu and toolbar item keys`](using-contextual-menu-and-toolbar-item-keys.md).

##### Localize the Toolbar Label

Provide an `InfoPlist.strings` file and include localized text for a custom key based on your toolbar identifier. For example, to provide a Polish translation for a toolbar item with an identifier of `translate`, add the following entry to your strings file:

```swift
"Toolbar Button Label for Identifier: translate" = "Przetłumacz";
```

For more information, see [`Managing Your App’s Information Property List`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list).

##### Dynamically Change the Image of a Toolbar Item

To update a toolbar item’s image dynamically, Safari uses the  [`setImage(_:)`](sfsafaritoolbaritem/setimage(_:).md) method for `SFSafariToolbarItem`. Setting the image to `nil` sets the default image.

##### Adjust the State of the Toolbar Item

Your app extension has the following control over the toolbar item:

- The app extension can enable or disable the button. Use [`setEnabled(_:)`](sfsafaritoolbaritem/setenabled(_:).md) if your toolbar item is usable only some of the time.
- The app extension can add a string to the toolbar item as a badge. For example, if your extension contains a list of items that the user can see by clicking the button, you might add a badge to the toolbar item using [`setBadgeText(_:)`](sfsafaritoolbaritem/setbadgetext(_:).md) with the number of unread items.

State changes can trigger in either of the following ways:

- Based on the user’s actions, Safari can implement a change to the button’s state.
- Your app extension can force a state change to happen explicitly.

> ❗ **Important**:  An injected content script can’t directly force the toolbar item to become enabled or disabled. However, you can implement this control yourself by sending a message to your app extension, and changing the toolbar state in your message handler. For more information, see [`Passing messages between Safari app extensions and injected scripts`](passing-messages-between-safari-app-extensions-and-injected-scripts.md).

##### Validate the Safari Toolbar Item

When an event occurs that may require your toolbar’s state to change, Safari calls your app extension’s event handler. The event handler receives parameters that indicate the window the toolbar appears in, and a completion handler for your app extension to call. Your event handler determines whether to enable or disable the toolbar button and whether to display a badge, and then returns this information to Safari.

The code below shows one possible implementation of the [`validateToolbarItem(in:validationHandler:)`](sfsafariextensionhandling/validatetoolbaritem(in:validationhandler:).md)method. In this case, the app extension has a list of items that it keeps track of, and it adds a badge to the toolbar item with the number of available items.

##### Set the Toolbar Information Explicitly

If you have a reference to an [`SFSafariWindow`](sfsafariwindow.md) object, you can use it to get a proxy object for the toolbar item, and then use that object to set the toolbar’s status directly.

##### Add Commands to the Toolbar Item

If you configure your toolbar item to send a command, clicking the toolbar button in Safari calls your extension handler’s [`toolbarItemClicked(in:)`](sfsafariextensionhandling/toolbaritemclicked(in:).md) method. You can then process the event however you like. The window passes in as a parameter, so this code retrieves the toolbar item for that window and updates its badge.

Another common usage when the toolbar item activates is to forward the message to an injected script on the page, so that you can modify the page in some way. The code below shows one possible way to forward the toolbar action. This code retrieves the active tab on the window that the user clicks, uses the tab to retrieve the page, and then dispatches a message to the page.

##### Display a Popover for a Toolbar Item

A popover is a window that pops up over an active window when the user clicks a toolbar button — no navigation is necessary. You can use a popover to show a small amount of information or to complete a small action. The popover closes automatically when the user changes focus (by clicking another window, for example). The [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/guidelines/overview) describe how to best use popovers.

In a Safari app extension, you implement the popover content using native view and view controller objects based on AppKit. When your native app and your Safari app extension share the same data model, this design also makes it easier to share other pieces of view code between the two. Safari and the operating system do all of the work to display this content within the Safari browser and to process events as they come in.

You implement your popover as a subclass of [`SFSafariExtensionViewController`](sfsafariextensionviewcontroller.md). As with other macOS development, typically you add your own outlets and actions to the view controller, and provide an XIB file for its user interface. The Xcode template for a Safari app extension provides some boilerplate code to get you started. Use Auto Layout so that your content adapts to different sizes.

If you configure your toolbar item to display a popover, clicking the toolbar button in Safari calls your extension handler’s [`popoverViewController()`](sfsafariextensionhandling/popoverviewcontroller().md) method. Your app extension instantiates and returns the popover view controller. In the template, the popover implements as a singleton object.

Before displaying the popover, the system calls your handler’s [`popoverWillShow(in:)`](sfsafariextensionhandling/popoverwillshow(in:).md) method. You can use this method to populate the contents of the window with new information. Similarly, after the popover disappears, the system calls the handler’s [`popoverDidClose(in:)`](sfsafariextensionhandling/popoverdidclose(in:).md) method so that you can perform any necessary cleanup.

## See Also

- [Using contextual menu and toolbar item keys](using-contextual-menu-and-toolbar-item-keys.md)
  Learn about adding contextual menu items and toolbar items to a Safari app extension with information property list keys.
- [Adjusting settings for contextual menu items](adjusting-settings-for-contextual-menu-items.md)
  Customize contextual menu items for your Safari app extension.
- [class SFSafariToolbarItem](sfsafaritoolbaritem.md)
  A proxy for a Safari app extension toolbar item in a Safari window.
- [class SFSafariExtensionViewController](sfsafariextensionviewcontroller.md)
  The view controller for a popover associated with your app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/adjusting-settings-for-a-toolbar-item)*