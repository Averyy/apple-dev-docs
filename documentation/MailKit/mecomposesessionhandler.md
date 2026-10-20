# MEComposeSessionHandler

**Framework**: MailKit  
**Kind**: protocol  
**Role**: Protocol

An object that participates in the composition of mail messages, and annotates recipient tokens.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
protocol MEComposeSessionHandler : NSObjectProtocol
```

```objc
@protocol MEComposeSessionHandler <NSObject>
```

#### Overview

When the user composes a message, MailKit requests a compose session handler object from your extension. MailKit uses this handler in the following ways:

- To inform it when the compose session begins and ends
- To add status annotations for email addresses that the user enters into the To, Cc, and Bcc fields
- To display a custom popover in the compose window
- To include custom headers in an outgoing message
- To confirm that an outgoing message is ready for delivery

Each of the items in the list above corresponds to methods that the handler implements.

To indicate that your extension contains a compose session handler, add `MEComposeSessionHandler` to the [`MEExtensionCapabilities`](../BundleResources/information-property-list/nsextension/nsextensionattributes/meextensioncapabilities.md) array in the extension’s `Info.plist` file:

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
- [class MEComposeSession](./mecomposesession.md)
  An object that represents a single mail compose window.
- [func mailComposeSessionDidBegin(MEComposeSession)](./mecomposesessionhandler/mailcomposesessiondidbegin%28_%29.md)
  Informs the handler when the user opens a compose window.
- [func mailComposeSessionDidEnd(MEComposeSession)](./mecomposesessionhandler/mailcomposesessiondidend%28_%29.md)
  Informs the handler when the user closes a compose window.
- [struct MEComposeSessionError](./mecomposesessionerror.md)
  An error that indicates the compose session is in an erroneous state.
### Annotating Email Address Tokens
- [func annotateAddressesForSession(MEComposeSession, completion: ([MEEmailAddress : MEAddressAnnotation]) -> Void)](./mecomposesessionhandler/annotateaddressesforsession%28_,completion%29.md)
  Indicates whether recipients in the compose window are valid or not.
- [class MEAddressAnnotation](./meaddressannotation.md)
  An object that indicates the validity of an email address.
### Extending the Compose Window Interface
- [func viewController(for: MEComposeSession) -> MEExtensionViewController](./mecomposesessionhandler/viewcontroller%28for%29.md)
  Provides a custom view controller to display as part of the compose window.
### Adding Custom Headers
- [func additionalHeaders(for: MEComposeSession) -> [String : [String]]](./mecomposesessionhandler/additionalheaders%28for%29.md)
  Provides custom headers to include in the outgoing message.
### Approving Message Delivery
- [func allowMessageSendForSession(MEComposeSession, completion: ((any Error)?) -> Void)](./mecomposesessionhandler/allowmessagesendforsession%28_,completion%29.md)
  Confirms that the message is ready for delivery.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesessionhandler)*