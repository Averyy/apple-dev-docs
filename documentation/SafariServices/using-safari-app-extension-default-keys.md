# Using Safari app extension default keys

**Framework**: Safari Services

Learn about the default keys in the information property list file.

#### Overview

After you create a Safari app extension target in Xcode, you need to modify the information property list file, `Info.plist.` You make changes to identify your new Safari app extension, and specify its capabilities and access limits under the `NSExtension` key.

The keys under the `NSExtension` key apply to the Safari app extension point, `com.apple.Safari.extension` for macOS. Place these keys as subordinates of the `NSExtension` key.

A Safari app extension includes these entries by default:

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