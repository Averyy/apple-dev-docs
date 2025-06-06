# MEComposeSessionError.Code

**Framework**: MailKit  
**Kind**: enum

Errors that indicate invalid compose session states.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum Code
```

## Topics

### Indicating Erroneous States
- [MEComposeSessionError.Code.invalidBody](mecomposesessionerror/code/invalidbody.md)
  An error code that indicates the message’s body is invalid.
- [MEComposeSessionError.Code.invalidHeaders](mecomposesessionerror/code/invalidheaders.md)
  An error code that indicates one or more of the message’s headers are invalid.
- [MEComposeSessionError.Code.invalidRecipients](mecomposesessionerror/code/invalidrecipients.md)
  An error code that indicates one or more of the message’s recipients are invalid.
### Initializers
- [init?(rawValue: Int)](mecomposesessionerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MEComposeUserAction](mecomposeuseraction.md)
- [MEMessageAction.Flag](memessageaction/flag.md)
- [enum MEMessageEncryptionState](memessageencryptionstate.md)
- [MEMessageSecurityError.Code](memessagesecurityerror/code.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesessionerror/code)*