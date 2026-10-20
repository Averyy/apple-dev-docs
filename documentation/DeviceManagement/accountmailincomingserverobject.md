# AccountMailIncomingServerObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The settings for the incoming mail server for this account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.1+

## Declaration

```
object AccountMailIncomingServerObject
```

## Properties

- `AuthenticationCredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials for this account to authenticate with an incoming mail server. The corresponding asset must be of type `CredentialUserNameAndPassword`.

  If the `AuthenticationMethod` is `None`, this field must be blank. Otherwise, the declaration must contain this field.
- `AuthenticationMethod` (string) *(required)*: The authentication method for the incoming mail server.

  **Allowed Values**: `None`, `Password`, `CRAMMD5`, `NTLM`, `HTTPMD5`
- `HostName` (string) *(required)*: The host name for the incoming mail server.
- `IMAPPathPrefix` (string): The path prefix for the IMAP server. The system uses this only when `ServerType` is `IMAP`.
- `Port` (integer): The port number for the incoming mail server.
- `ServerType` (string) *(required)*: The mail protocol this account uses.

  **Allowed Values**: `IMAP`, `POP`

## See Also

### Objects
- [object AccountMailOutgoingServerObject](./accountmailoutgoingserverobject.md)
  The settings for the outgoing mail server for this account.
- [object AccountMailSMIMEObject](./accountmailsmimeobject.md)
  Settings for S/MIME.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountmailincomingserverobject)*