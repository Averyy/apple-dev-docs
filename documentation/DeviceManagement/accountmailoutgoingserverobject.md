# AccountMailOutgoingServerObject

**Framework**: Device Management  
**Kind**: dictionary

The settings for the outgoing mail server for this account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```swift
object AccountMailOutgoingServerObject
```

## Properties

- `AuthenticationCredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials for this account to authenticate with an outgoing mail server. The corresponding asset must be of type `CredentialUserNameAndPassword`. If the `AuthenticationMethod` is `None`, this field must be blank. Otherwise, the declaration must contain this field.
- `AuthenticationMethod` (string) *(required)*: The authentication method for the outgoing mail server.
- `HostName` (string) *(required)*: The host name for the outgoing mail server.
- `Port` (integer): The port number for the outgoing mail server.

## See Also

- [object AccountMailIncomingServerObject](accountmailincomingserverobject.md)
  The settings for the incoming mail server for this account.
- [object AccountMailSMIMEObject](accountmailsmimeobject.md)
  Settings for S/MIME.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountmailoutgoingserverobject)*