# signingIdentity

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Allows access to the signing identity, if present in the JPKI applet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
let signingIdentity: JPKIPassContents.SigningIdentity?
```

## See Also

- [func changePassword(from: String, to: String) async throws](jpkipasscontents/signingidentity-swift.struct/changepassword(from:to:).md)
  A function that allows you to change the password associated with the signing identity.
- [JPKIPassContents.SigningIdentity.AuthenticationType](jpkipasscontents/signingidentity-swift.struct/authenticationtype.md)
  Defines the valid user authentication request options for the signing identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/signingidentity-swift.property)*