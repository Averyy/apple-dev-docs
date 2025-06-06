# MailKit

**Framework**: MailKit  
**Kind**: module

Secure, customize, and act on email messages that users send and receive.

**Availability**:
- macOS 12.0+

#### Overview

MailKit lets your app include an app extension that customizes several features of Mail. A Mail app extension provides one or more of the following enhancements:

- A  defines rules to prevent loading content when users view messages.
- An  performs actions such as flagging, setting colors, or archiving when Mail downloads messages.
- A  validates recipient email addresses, displays a view controller on Mail’s compose windows, confirms if messages are suitable for delivery, and adds custom headers.
- A  secures messages using encryption and digital signatures.

The entry point for your extension is an object that conforms to [`MEExtension`](meextension.md). When MailKit invokes your extension, this objects determines the handlers that provide each capability in the list above.

## Topics

### Essentials
- [protocol MEExtension](meextension.md)
  A type that provides objects for manipulating email messages, such as performing actions on messages or blocking content when users view messages.
- [Build Mail App Extensions](build-mail-app-extensions.md)
  Create app extensions that block content, perform message and composing actions, and help message security.
### Content Blockers
- [protocol MEContentBlocker](mecontentblocker.md)
  An object that provides a set of rules to block content when displaying a message.
### Message Actions
- [protocol MEMessageActionHandler](memessageactionhandler.md)
  An object that performs actions on messages as the system downloads them.
### Compose Window Enhancements
- [protocol MEComposeSessionHandler](mecomposesessionhandler.md)
  An object that participates in the composition of mail messages, and annotates recipient tokens.
### Message Encryption, Decryption, and Digital Signatures
- [protocol MEMessageSecurityHandler](memessagesecurityhandler.md)
  An object that digitally signs or encrypts messages the user sends and receives.
### Message Properties
- [class MEMessage](memessage.md)
  An object that contains information about a mail message, such as the subject, addressees, date sent, and the message contents.
- [enum MEMessageState](memessagestate.md)
  The state of a message: sent, unsent, or received.
### Custom View Controllers
- [class MEExtensionViewController](meextensionviewcontroller.md)
  An object that manages a view for compose session and message security handlers.
### Structures
- [struct MEMessageSecurityError](memessagesecurityerror.md)
### Classes
- [class MEComposeContext](mecomposecontext.md)
- [class MEDecodedMessageBanner](medecodedmessagebanner.md)
- [class MEEmailAddress](meemailaddress.md)
- [class MEExtensionManager](meextensionmanager.md)
### Reference
- [MailKit Enumerations](mailkit-enumerations.md)
- [MailKit Constants](mailkit-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/MailKit)*