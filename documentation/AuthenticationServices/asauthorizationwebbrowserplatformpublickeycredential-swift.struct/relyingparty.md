# relyingParty

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The relying party that issues challenges for this credential.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 16.4+
- macOS 13.3+

## Declaration

```swift
let relyingParty: String
```

## See Also

### Describing credentials
- [let customTitle: String](./customtitle.md)
  A string the person can supply to describe this credential.
- [let name: String](./name.md)
  The user name for the account associated with this credential.
- [let providerName: String](./providername.md)
  The name of the app that manages this credential, or “iCloud Keychain” if it’s the operating system.
- [let userHandle: Data](./userhandle.md)
  A unique identifier for the user account at the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationwebbrowserplatformpublickeycredential-swift.struct/relyingparty)*