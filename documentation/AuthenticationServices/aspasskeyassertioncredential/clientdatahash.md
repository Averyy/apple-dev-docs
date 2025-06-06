# clientDataHash

**Framework**: Authentication Services  
**Kind**: property

A hash of the client data for this credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var clientDataHash: Data { get }
```

## See Also

- [var authenticatorData: Data](aspasskeyassertioncredential/authenticatordata.md)
  The authenticator data of the application that created this passkey assertion credential.
- [var credentialID: Data](aspasskeyassertioncredential/credentialid.md)
  The identifier for this credential.
- [var relyingParty: String](aspasskeyassertioncredential/relyingparty.md)
  The relying party associated with this passkey.
- [var signature: Data](aspasskeyassertioncredential/signature.md)
  The cryptographic signature of this credential.
- [var userHandle: Data](aspasskeyassertioncredential/userhandle.md)
  The user handle of this passkey.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredential/clientdatahash)*