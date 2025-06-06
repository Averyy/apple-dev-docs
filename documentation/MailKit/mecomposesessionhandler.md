# MEComposeSessionHandler

**Framework**: MailKit  
**Kind**: protocol

An object that participates in the composition of mail messages, and annotates recipient tokens.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
protocol MEComposeSessionHandler : NSObjectProtocol
```

#### Overview

When the user composes a message, MailKit requests a compose session handler object from your extension. MailKit uses this handler in the following ways:

- To inform it when the compose session begins and ends
- To add status annotations for email addresses that the user enters into the To, Cc, and Bcc fields
- To display a custom popover in the compose window
- To include custom headers in an outgoing message
- To confirm that an outgoing message is ready for delivery

Each of the items in the list above corresponds to methods that the handler implements.

To indicate that your extension contains a compose session handler, add `MEComposeSessionHandler` to the [`MEExtensionCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/MEExtensionCapabilities) array in the extension’s `Info.plist` file:

```swift
<key>NSExtensionAttributes</key>
<dict>
    <key>MEExtensionCapabilities</key>
    <array>
        <string>MEComposeSessionHandler</string>
    </array>
</dict>
```

## Topics

### Handling Compose Sessions
- [class MEComposeSession](mecomposesession.md)
  An object that represents a single mail compose window.
- [func mailComposeSessionDidBegin(MEComposeSession)](mecomposesessionhandler/mailcomposesessiondidbegin(_:).md)
  Informs the handler when the user opens a compose window.
- [func mailComposeSessionDidEnd(MEComposeSession)](mecomposesessionhandler/mailcomposesessiondidend(_:).md)
  Informs the handler when the user closes a compose window.
- [struct MEComposeSessionError](mecomposesessionerror.md)
  An error that indicates the compose session is in an erroneous state.
### Annotating Email Address Tokens
- [func annotateAddressesForSession(MEComposeSession, completion: ([MEEmailAddress : MEAddressAnnotation]) -> Void)](mecomposesessionhandler/annotateaddressesforsession(_:completion:).md)
  Indicates whether recipients in the compose window are valid or not.
- [class MEAddressAnnotation](meaddressannotation.md)
  An object that indicates the validity of an email address.
### Extending the Compose Window Interface
- [func viewController(for: MEComposeSession) -> MEExtensionViewController](mecomposesessionhandler/viewcontroller(for:).md)
  Provides a custom view controller to display as part of the compose window.
### Adding Custom Headers
- [func additionalHeaders(for: MEComposeSession) -> [String : [String]]](mecomposesessionhandler/additionalheaders(for:).md)
  Provides custom headers to include in the outgoing message.
### Approving Message Delivery
- [func allowMessageSendForSession(MEComposeSession, completion: ((any Error)?) -> Void)](mecomposesessionhandler/allowmessagesendforsession(_:completion:).md)
  Confirms that the message is ready for delivery.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesessionhandler)*