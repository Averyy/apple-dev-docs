# userIdentity

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Allows for access to the user identity, if present in the JPKI applet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
let userIdentity: JPKIPassContents.UserIdentity?
```

## See Also

- [func changePIN(from: String, to: String) async throws](jpkipasscontents/useridentity-swift.struct/changepin(from:to:).md)
  A function that allows for the change of the PIN associated with the user identity.
- [JPKIPassContents.UserIdentity.AuthenticationType](jpkipasscontents/useridentity-swift.struct/authenticationtype.md)
  Defines valid authentication types associated with the user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/useridentity-swift.property)*