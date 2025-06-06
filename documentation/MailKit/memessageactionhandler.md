# MEMessageActionHandler

**Framework**: MailKit  
**Kind**: protocol

An object that performs actions on messages as the system downloads them.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol MEMessageActionHandler : NSObjectProtocol
```

#### Overview

As MailKit downloads messages, it invokes the [`decideAction(for:completionHandler:)`](memessageactionhandler/decideaction(for:completionhandler:).md) method on your handler. You indicate the action to take for each message, such as marking it as read or unread, flagging it, or archiving it.

To indicate that your extension contains a message action handler, add `MEMessageActionHandler` to the [`MEExtensionCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/MEExtensionCapabilities) array in the extension’s `Info.plist` file:

```plist
<key>NSExtensionAttributes</key>
<dict>
    <key>MEExtensionCapabilities</key>
    <array>
        <string>MEMessageActionHandler</string>
    </array>
</dict>
```

## Topics

### Performing Actions on Messages
- [func decideAction(for: MEMessage, completionHandler: (MEMessageActionDecision?) -> Void)](memessageactionhandler/decideaction(for:completionhandler:).md)
  Determines the action that the system takes when it downloads a message.
- [class MEMessageAction](memessageaction.md)
  An action the system performs on a message, such as setting a color or archiving it.
- [class MEMessageActionDecision](memessageactiondecision.md)
  The action that the system performs on a message, or a request to ask the action handler again later when the message content is available.
- [MEMessageAction.MessageColor](memessageaction/messagecolor.md)
  A color that the system uses to display a message in the message list.
### Instance Properties
- [var requiredHeaders: [String]](memessageactionhandler/requiredheaders.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageactionhandler)*