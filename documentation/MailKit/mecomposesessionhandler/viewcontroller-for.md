# viewController(for:)

**Framework**: MailKit  
**Kind**: method  
**Required**: Yes

Provides a custom view controller to display as part of the compose window.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
func viewController(for session: MEComposeSession) -> MEExtensionViewController
```

#### Return Value

A custom [`MEExtensionViewController`](meextensionviewcontroller.md) subclass that Mail displays in the compose window.

#### Discussion

To configure an icon and tooltip for the compose session handler’s view controller, add the following entries to your extension’s `Info.plist` file:

```plist
<key>NSExtensionAttributes</key>
<dict>
    <key>MEComposeSession</key>
    <dict>
        <key>MEComposeIcon</key>
        <string>YourCustomComposeIconName</string>
        <key>MEComposeIconToolTip</key>
        <string>Tooltip for the compose session handler.</string>
    </dict>
<dict>
```

Include an icon in your extension’s bundle using the name you specify for [`MEComposeIcon`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/MEComposeSession/MEComposeIcon).

> 💡 **Tip**:  Include the icon in an asset catalog in your extension’s bundle, and include both light and dark variants.

## Parameters

- `session`: The session that represents the properties of the message in the compose window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesessionhandler/viewcontroller(for:))*