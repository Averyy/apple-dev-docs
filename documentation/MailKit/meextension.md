# MEExtension

**Framework**: MailKit  
**Kind**: protocol

A type that provides objects for manipulating email messages, such as performing actions on messages or blocking content when users view messages.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
protocol MEExtension : NSObjectProtocol
```

#### Overview

To implement an app extension, you provide an object that conforms to the [`MEExtension`](meextension.md) protocol. The [`MEExtensionCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/MEExtensionCapabilities) key of your extension’s `Info.plist` defines the capabilities that you support, as follows:

```plist
<key>NSExtensionAttributes</key>
<dict>
    <key>MEExtensionCapabilities</key>
    <array>
        <string>MEContentBlocker</string>
        <string>MEMessageActionHandler</string>
        <string>MEComposeSessionHandler</string>
        <string>MEMessageSecurityHandler</string>
    </array>
</dict>
```

For each capability that your extension defines, you provide an object that implements the capability. MailKit uses the following methods to request the object for a given capability. The capability also specifies a protocol that the handler implements.

| Capability Key | Method | Protocol |
| --- | --- | --- |
| `MEContentBlocker` | [`handler(for:)`](meextension/handler(for:).md) | [`MEContentBlocker`](mecontentblocker.md) |
| `MEMessageActionHandler` | [`handlerForMessageActions()`](meextension/handlerformessageactions().md) | [`MEMessageActionHandler`](memessageactionhandler.md) |
| `MEComposeSessionHandler` | [`handlerForContentBlocker()`](meextension/handlerforcontentblocker().md) | [`MEComposeSessionHandler`](mecomposesessionhandler.md) |
| `MEMessageSecurityHandler` | [`handlerForMessageSecurity()`](meextension/handlerformessagesecurity().md) | [`MEMessageSecurityHandler`](memessagesecurityhandler.md) |

## Topics

### Blocking Content
- [func handlerForContentBlocker() -> any MEContentBlocker](meextension/handlerforcontentblocker.md)
  Returns an object that provides rules that the message viewer uses to block content.
### Performing Actions on Messages
- [func handlerForMessageActions() -> any MEMessageActionHandler](meextension/handlerformessageactions.md)
  Returns an object that performs actions on mail messages as the system downloads them.
### Enhancing the Compose Window
- [func handler(for: MEComposeSession) -> any MEComposeSessionHandler](meextension/handler(for:).md)
  Returns an object that participates in the composition of a mail message.
### Encrypting and Signing Messages
- [func handlerForMessageSecurity() -> any MEMessageSecurityHandler](meextension/handlerformessagesecurity.md)
  Returns an object that applies security measures such as encryption and digital signatures to messages.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Build Mail App Extensions](build-mail-app-extensions.md)
  Create app extensions that block content, perform message and composing actions, and help message security.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meextension)*