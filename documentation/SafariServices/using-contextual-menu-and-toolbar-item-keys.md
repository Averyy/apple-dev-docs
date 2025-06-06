# Using contextual menu and toolbar item keys

**Framework**: Safariservices

Learn about adding contextual menu items and toolbar items to a Safari app extension with information property list keys.

#### Overview

Contextual menu items and toolbar items give you ways to add more menu options and entry points to your Safari app extension. You define and adjust these items using information property list keys.

##### Add Context Menu Items

The `SFSafariContextMenu` key lets your app extension add items to the context menu that appears in webpages. See [`Context menus`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/menus/contextual-menus/) for design guidelines.

![A screenshot of a context menu in Safari. It’s a vertical menu containing five options, including Reload Page and Inspect Element. ](https://docs-assets.developer.apple.com/published/c35ab9d49f9e8e49de2b754599fe084e/media-3027377%402x.png)

The key’s value must be an array, and must contain one dictionary with two subkeys for each menu item.

| Subkey | Type | Description |
| --- | --- | --- |
| `Text` | String | Required. A string that specifies the text to display for the context menu item. |
| `Command` | String | Required. A string that the context menu item sends when it activates. It contains the name of the command you want to send to your app extension when the user selects your item. |

For example, if you add two contextual menu items, your `Info.plist` file might look like the following:

```other
<key>SFSafariContextMenu</key>
<array>
	<dict>
		<key>Text</key>
		<string>Search for selected text in MyApplication.</string>
		<key>Command</key>
		<string>Search</string>
	</dict>
	<dict>
		<key>Text</key>
		<string>Add an entry for selected text in MyApplication.</string>
		<key>Command</key>
		<string>Add</string>
	</dict>
</array>
```

##### Add a Toolbar Item

The `SFSafariToolbarItem` dictionary adds a toolbar item to Safari windows. See [`Toolbars`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/windows-and-views/toolbars/) for design guidelines.

![A screenshot of a partial Safari toolbar. It shows standard toolbar items, as well as an app extension toolbar item that looks like a lightning bolt inside a circle. ](https://docs-assets.developer.apple.com/published/21e2316c9ce5a406ca193a4330baa8aa/media-3027375%402x.png)

Each app extension can have only one toolbar item. The value for this key is a dictionary that describes the toolbar item. There are four required keys for the toolbar item dictionary.

| Subkey | Type | Description |
| --- | --- | --- |
| `Identifier` | String | Required. A string identifier for the toolbar item. This doesn’t display to the user. |
| `Label` | String | Required. A string that appears in the overflow menu, in the Customize palette, and on hover. |
| `Image` | String | Required. A string specifying the filename of a scalable PDF image. The image must be transparent. Add the image file to your extension’s Xcode target. |
| `Action` | String | Required. A string specifying the command to send when the user clicks the toolbar item. Available actions are `Command` (to send a command to the app extension) and `Popover` (to display a popover window). This action determines which methods you need to implement to handle button events. |

Here’s an example dictionary in XML:

```other
<dict>
	<key>Action</key>
	<string>Command</string>
	<key>Identifier</key>
	<string>Button</string>
	<key>Image</key>
	<string>Toolbar.pdf</string>
	<key>Label</key>
	<string>My Item</string>
</dict>
```

Use the `Image` key to provide an image for the toolbar button. Safari may resize or recolor the toolbar button image when drawing it to the screen. Make your image a template image and follow the guidelines for toolbar items.

> **Note**:  Buttons on the Safari toolbar are largely transparent, allowing them to fill with the appropriate gradient for the current macOS user interface. You don’t need to draw the button itself.

## See Also

- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)
  Customize a toolbar item for your Safari app extension.
- [Adjusting settings for contextual menu items](adjusting-settings-for-contextual-menu-items.md)
  Customize contextual menu items for your Safari app extension.
- [class SFSafariToolbarItem](sfsafaritoolbaritem.md)
  A proxy for a Safari app extension toolbar item in a Safari window.
- [class SFSafariExtensionViewController](sfsafariextensionviewcontroller.md)
  The view controller for a popover associated with your app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SafariServices/using-contextual-menu-and-toolbar-item-keys)*