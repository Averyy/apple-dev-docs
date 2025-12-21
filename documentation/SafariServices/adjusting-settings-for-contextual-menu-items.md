# Adjusting settings for contextual menu items

**Framework**: Safari Services

Customize contextual menu items for your Safari app extension.

#### Overview

You can add items to the contextual menu that Safari shows when the user Control-clicks a webpage. These actions trigger the following sequence of events:

1. Safari sends an event to the web document, informing it that a contextual menu is about to appear.
2. Safari displays the contextual menu.
3. If the user chooses one of the items associated with your app extension, Safari calls your app extension’s handler to perform the command.

To learn how to add a contextual menu item, see [`Using contextual menu and toolbar item keys`](using-contextual-menu-and-toolbar-item-keys.md).

##### Localize the Contextual Menu Item

To localize a contextual menu, provide an `InfoPlist.strings` file and include localized text for a custom key based on your command string. For example, to provide a Polish translation for a menu item with a command string of `Add`, you add the following entry to your strings file:

```swift
"Context Menu Item Label for Command: Add" = "Dodaj";

```

For more information, see [`Managing your app’s information property list values`](https://developer.apple.com/documentation/BundleResources/managing-your-app-s-information-property-list#Localize-the-Information-Property-List).

##### Validate and Change Text in a Contextual Menu Item

Use the [`validateContextMenuItem(withCommand:in:userInfo:validationHandler:)`](sfsafariextensionhandling/validatecontextmenuitem(withcommand:in:userinfo:validationhandler:).md) method to validate a contextual menu item. The command parameter is the `Command` string you provide in the `Info.plist` entry for the menu item. The `validationHandler` parameter is a code block where you specify whether to hide the menu item, and what text to use for it. Using this option, you can dynamically change the text of a context menu item.

To change the menu text, use the following code:

To use the default text, use the following code:

To hide the menu item, use the following code:

##### Send Custom Information to Your App Extension

To pass information from the current webpage to your app extension when the user chooses your menu item, you need to inject a JavaScript file; see [`Injecting a script into a webpage`](injecting-a-script-into-a-webpage.md). When the user Control-clicks a webpage, Safari sends out a `contextmenu` event. Your script can add a listener for this event, and react to it by inserting information into the user info dictionary. If the user later selects one of your contextual menu items, Safari sends this dictionary when it calls your app extension.

For example, to capture the currently selected text in a webpage, use the following code:

```javascript
document.addEventListener("contextmenu", handleContextMenu, false);
function handleContextMenu(event) {
    var selectedText =  window.getSelection().toString();
    safari.extension.setContextMenuEventUserInfo(event,
        { "selectedText": selectedText });
}
```

##### Handle Contextual Menu Item Commands in Your App Extension

When the user selects one of your contextual menu items, Safari sends the [`contextMenuItemSelected(withCommand:in:userInfo:)`](sfsafariextensionhandling/contextmenuitemselected(withcommand:in:userinfo:).md) method to your [`SFSafariExtensionHandler`](sfsafariextensionhandler.md) subclass. The `c`ommand parameter is the `Command` string you provide in the `Info.plist` entry for the menu item.

For example, if you add the `Command` string in your `Info.plist` entries for a contextual menu item, you might implement your context menu method to perform different actions for different commands.

You can use the `page` parameter to access information about the current webpage, including the URL and page title, and to send messages back to your injected JavaScript file using the [`dispatchMessageToScript(withName:userInfo:)`](sfsafaripage/dispatchmessagetoscript(withname:userinfo:).md) method.

## See Also

- [Using contextual menu and toolbar item keys](using-contextual-menu-and-toolbar-item-keys.md)
  Learn about adding contextual menu items and toolbar items to a Safari app extension with information property list keys.
- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)
  Customize a toolbar item for your Safari app extension.
- [class SFSafariToolbarItem](sfsafaritoolbaritem.md)
  A proxy for a Safari app extension toolbar item in a Safari window.
- [class SFSafariExtensionViewController](sfsafariextensionviewcontroller.md)
  The view controller for a popover associated with your app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/adjusting-settings-for-contextual-menu-items)*