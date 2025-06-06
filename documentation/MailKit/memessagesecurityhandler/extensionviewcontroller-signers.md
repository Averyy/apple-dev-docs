# extensionViewController(signers:)

**Framework**: MailKit  
**Kind**: method  
**Required**: Yes

Returns a view controller that displays details about a message’s digital signature.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
func extensionViewController(signers messageSigners: [MEMessageSigner]) -> MEExtensionViewController?
```

#### Return Value

A view controller that users can display to see information about a message’s digital signature.

## Parameters

- `messageSigners`: An array that contains details about who signed the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityhandler/extensionviewcontroller(signers:))*