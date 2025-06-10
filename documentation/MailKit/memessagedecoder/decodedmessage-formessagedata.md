# decodedMessage(forMessageData:)

**Framework**: MailKit  
**Kind**: method  
**Required**: Yes

Decrypts message content and details about digital signatures.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func decodedMessage(forMessageData data: Data) -> MEDecodedMessage?
```

#### Return Value

An object that represents the decoded message, or `nil` if the message isn’t encrypted or signed.

#### Discussion

When MailKit needs the original unencoded data for a message, it invokes this method and passes the raw MIME data for the message. If you determine that the message isn’t encoded and your extension doesn’t need to do anything, return `nil,` and MailKit decodes the message data normally.

If you inspect the message data and determine that you need to decode it, create an instance of [`MEMessageSecurityInformation`](memessagesecurityinformation.md) that describes the message’s signed and encrypted status. If the message is signed, specify an array of [`MEMessageSigner`](memessagesigner.md) objects to indicate who signed the message. [`MEMessageSigner`](memessagesigner.md) includes additional context that the security handler’s view controller uses to display details to the user, such as the certificate a signer used.

To provide the decoded message content to MailKit, create an instance of [`MEDecodedMessage`](medecodedmessage.md). The decoded message contains the raw MIME content for the message, and the message security information.

> ❗ **Important**:  If decrypting the message fails, or the digital signature isn’t valid, include an error object with a localized description of the failure in the [`MEMessageSecurityInformation`](memessagesecurityinformation.md). Mail uses this description to inform the user of the issue.

## Parameters

- `data`: The raw MIME message data, which may be encrypted or signed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagedecoder/decodedmessage(formessagedata:))*