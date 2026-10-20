# MEComposeSessionError.Code

**Framework**: MailKit  
**Kind**: enum  
**Role**: Enumeration

Errors that indicate invalid compose session states.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum Code
```

```c
enum MEComposeSessionErrorCode : NSInteger;
```

## Topics

### Indicating Erroneous States
- [MEComposeSessionError.Code.invalidBody](./code/invalidbody.md)
  An error code that indicates the message’s body is invalid.
- [MEComposeSessionError.Code.invalidHeaders](./code/invalidheaders.md)
  An error code that indicates one or more of the message’s headers are invalid.
- [MEComposeSessionError.Code.invalidRecipients](./code/invalidrecipients.md)
  An error code that indicates one or more of the message’s recipients are invalid.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum MEComposeUserAction](../mecomposeuseraction.md)
- [MEMessageAction.Flag](../memessageaction/flag.md)
- [enum MEMessageEncryptionState](../memessageencryptionstate.md)
- [MEMessageSecurityError.Code](../memessagesecurityerror/code.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesessionerror/code)*