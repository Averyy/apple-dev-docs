# Setting Safari app extension feature keys

**Framework**: Safari Services

Set keys for permissions, scripts, style sheets, contextual menu items, and toolbar items in the information property list file.

#### Overview

After selecting which default keys to use in your Safari app extension’s information property list file, select the appropriate feature keys to identify files and UI items.

The table below lists the primary keys in the `NSExtension` dictionary that are associated with Safari app extension features. For information on available subkeys, see the link in the primary key description.

| Key | Type | Description |
| --- | --- | --- |
| `SFSafariContentScript` | Array | An array for adding content scripts to the extension. Each value in the array is a dictionary that provides the filename for a content script. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For subkeys, see [`Using content script and style sheet keys`](using-content-script-and-style-sheet-keys.md). |
| `SFSafariContextMenu` | Array | An array for adding items to Safari’s context menu — the menu that appears when the user Control-clicks a webpage. For more information, see [`Adjusting settings for contextual menu items`](adjusting-settings-for-contextual-menu-items.md). ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For subkeys, see [`Using contextual menu and toolbar item keys`](using-contextual-menu-and-toolbar-item-keys.md). |
| `SFSafariStyleSheet` | Array | An array for adding style sheets to the extension or to pages from a limited subset of URLs. Each value in the array is a dictionary that provides the filename for a content script. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For subkeys, see [`Using content script and style sheet keys`](using-content-script-and-style-sheet-keys.md). For more information, see [`Injecting CSS style sheets into a webpage`](injecting-css-style-sheets-into-a-webpage.md). |
| `SFSafariToolbarItem` | Dictionary | A dictionary for adding a toolbar item to Safari windows. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For subkeys, see [`Using contextual menu and toolbar item keys`](using-contextual-menu-and-toolbar-item-keys.md). |
| `SFSafariWebsiteAccess` | Dictionary | An optional dictionary that specifies which webpages the Safari app extension can access, if any. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) For details about configuring website access, see [`Adjusting website access permissions`](adjusting-website-access-permissions.md). |

In addition to the `NSExtension` keys, the `Info.plist` file includes an `NSHumanReadableDescription` key for your Safari app extension. When you install the app extension, the string value of this key appears in Safari > Settings > Preferences as the example below shows:

![A screenshot of the description that appears in Safari > Settings > Preferences when a user selects your extension. A heading reads My Extension 1.0 from FirstSafariExtensionApp. Below that, a description reads This is a Safari Extension. You should tell us what your extension does here. At the bottom is a button labeled Uninstall. ](https://docs-assets.developer.apple.com/published/231cabb59d94fbc04ffaa54d81f36828/media-3897929%402x.png)

## See Also

- [Adjusting website access permissions](adjusting-website-access-permissions.md)
  Set website access permissions in a Safari app extension using information property list keys.
- [Using permissions for scripts and style sheets](using-permissions-for-scripts-and-style-sheets.md)
  Learn about URL permissions for scripts and style sheets in a Safari app extension using information property list keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/setting-safari-app-extension-feature-keys)*