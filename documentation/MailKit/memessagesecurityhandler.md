# MEMessageSecurityHandler

**Framework**: Mailkit  
**Kind**: protocol

An object that digitally signs or encrypts messages the user sends and receives.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
protocol MEMessageSecurityHandler : MEMessageDecoder, MEMessageEncoder
```

#### Overview

When users enable an extension that implements a message security handler, Mail passes incoming and outgoing message content to the extension for encryption and digital signing.

To encompass the symmetrical halves for encoding and decoding, MailKit defines two protocols that [`MEMessageSecurityHandler`](memessagesecurityhandler.md) conforms to:

As the user composes a mail message, MailKit calls [`getEncodingStatus(for:composeContext:completionHandler:)`](memessageencoder/getencodingstatus(for:composecontext:completionhandler:).md) to determine if the handler can sign or encrypt the message. The handler indicates the capabilities by providing an instance of [`MEOutgoingMessageEncodingStatus`](meoutgoingmessageencodingstatus.md). Mail reflects this status in the compose window by enabling the appropriate buttons to let the user choose how to encode the message. When the user sends the message, MailKit invokes the [`encode(_:composeContext:completionHandler:)`](memessageencoder/encode(_:composecontext:completionhandler:).md) method, and indicates whether the user chose to encrypt or sign the message.

When MailKit needs the original message content, it invokes the handler’s [`decodedMessage(forMessageData:)`](memessagedecoder/decodedmessage(formessagedata:).md) method. This method creates an instance of [`MEDecodedMessage`](medecodedmessage.md) that includes the raw decoded message data and the details of who signed the message in an instance of [`MEMessageSecurityInformation`](memessagesecurityinformation.md).

> **Note**:  MailKit stores the encrypted and signed message content. Therefore, MailKit may ask a message security handler to decode the same message repeatedly over time when it needs the decoded original message content.

To indicate that your extension contains a message security handler, add `MEMessageSecurityHandler` to the [`MEExtensionCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/MEExtensionCapabilities) array in the extension’s `Info.plist` file:

```plist
<key>NSExtensionAttributes</key>
<dict>
    <key>MEExtensionCapabilities</key>
    <array>
        <string>MEMessageSecurityHandler</string>
    </array>
</dict>
```

## Topics

### Encrypting and Signing Messages
- [protocol MEMessageEncoder](memessageencoder.md)
  An object that encrypts or digitally signs outgoing messages.
- [class MEEncodedOutgoingMessage](meencodedoutgoingmessage.md)
  An object that contains the signed or encrypted representation of a message’s RFC 2822 data.
- [class MEOutgoingMessageEncodingStatus](meoutgoingmessageencodingstatus.md)
  An object that contains information about security measures the user can apply when composing a message.
- [class MEMessageEncodingResult](memessageencodingresult.md)
  An object that contains a signed or encrypted message, or errors that indicate failure to encode the message.
### Decrypting Messages and Verifying Signatures
- [protocol MEMessageDecoder](memessagedecoder.md)
  An object that decrypts messages and provides details about digital signatures.
- [class MEDecodedMessage](medecodedmessage.md)
  An object that contains the RFC 2822 data for a message, without encryption or digital signatures.
- [class MEMessageSigner](memessagesigner.md)
  An object that contains details about the person who signed a message.
- [class MEMessageSecurityInformation](memessagesecurityinformation.md)
  An object that contains details about a message’s content, such as if it’s encrypted and who digitally signed it.
### Displaying Signature Details
- [func extensionViewController(signers: [MEMessageSigner]) -> MEExtensionViewController?](memessagesecurityhandler/extensionviewcontroller(signers:).md)
  Returns a view controller that displays details about a message’s digital signature.
### Instance Methods
- [func extensionViewController(messageContext: Data) -> MEExtensionViewController?](memessagesecurityhandler/extensionviewcontroller(messagecontext:).md)
- [func primaryActionClicked(forMessageContext: Data, completionHandler: (MEExtensionViewController?) -> Void)](memessagesecurityhandler/primaryactionclicked(formessagecontext:completionhandler:).md)

## Relationships

### Inherits From
- [MEMessageDecoder](memessagedecoder.md)
- [MEMessageEncoder](memessageencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/MailKit/memessagesecurityhandler)*