# Using Safari app extension default keys

**Framework**: Safari Services

Learn about the default keys in the information property list file.

#### Overview

After you create a Safari app extension target in Xcode, you need to modify the information property list file, `Info.plist.` You make changes to identify your new Safari app extension, and specify its capabilities and access limits under the `NSExtension` key.

The keys under the `NSExtension` key apply to the Safari app extension point, `com.apple.Safari.extension` for macOS. Place these keys as subordinates of the `NSExtension` key.

A Safari app extension includes these entries by default:

- **`NSExtensionPointIdentifier`**: An identifier string to indicate a Safari extension: `com.apple.Safari.extension`.
- **`NSExtensionPrincipalClass`**: A string to indicate the class with the principal implementation for your extension, with a value of `SafariExtensionHandler`, which the `SafariExtensionHandler.swift` file defines in Swift, and the `SafariExtensionHandler.h` and `SafariExtensionHandler.m` files define in Objective-C.
- **`SFSafariContentScript`**: An array of dictionaries with a single entry, containing a `Script` key that specifies the `script.js` file in the template. When your extension loads, Safari automatically embeds this script file into every webpage that a user visits and the extension has access to. See [`Injecting a script into a webpage`](injecting-a-script-into-a-webpage.md).
- **`SFSafariToolbarItem`**: A dictionary describing a toolbar item that uses the `ToolbarItemIcon.pdf` image from the template as the image for the button. See [`Adjusting settings for a toolbar item`](adjusting-settings-for-a-toolbar-item.md).
- **`SFSafariWebsiteAccess`**: A dictionary with two keys: the `Level` key to indicate the level of access (set to `Some`), and the `Allowed Domains` key, which includes an array of strings to limit the web addresses that your extension works with. For more information, see [`Adjusting website access permissions`](adjusting-website-access-permissions.md).

Although `SFSafariContentScript`, `SFSafariToolbarItem`, and `SFSafariWebsiteAccess` are all default keys, they’re not required because they specify features that may or may not exist in your Safari app extension. To learn more about feature keys, see [`Setting Safari app extension feature keys`](setting-safari-app-extension-feature-keys.md).

##### Review the Sample Information Property List

The code example below represents the overall structure of a typical `NSExtension` dictionary. Keep this structure in mind as you configure each element of your app extension.

```other
<dict>
	<key>NSExtensionPointIdentifier</key>
	<string>com.apple.Safari.extension</string>
	<key>NSExtensionPrincipalClass</key>
	<string>SafariExtensionHandler</string>
	<key>SFSafariToolbarItem</key>
	<dict>
		<key>Action</key>
		<string>Command</string>
		<key>Identifier</key>
		<string>Button</string>
		<key>Image</key>
		<string>ToolbarItemIcon.pdf</string>
		<key>Label</key>
		<string>Your Button</string>
	</dict>
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
	<key>SFSafariContentScript</key>
	<array>
		<dict>
			<key>Script</key>
			<string>script.js</string>
		</dict>
	</array>
	<key>SFSafariStyleSheet</key>
	<array>
		<dict>
			<key>Style Sheet</key>
			<string>style.css</string>
		</dict>
	</array>
	<key>SFSafariWebsiteAccess</key>
	<dict>
		<key>Allowed Domains</key>
		<array>
			<string>*.webkit.org</string>
		</array>
		<key>Level</key>
		<string>Some</string>
	</dict>
</dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/using-safari-app-extension-default-keys)*