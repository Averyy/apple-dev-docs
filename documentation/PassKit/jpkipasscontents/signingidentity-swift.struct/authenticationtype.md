# JPKIPassContents.SigningIdentity.AuthenticationType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Defines the valid user authentication request options for the signing identity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum AuthenticationType
```

## Topics

### Case for authentication
- [JPKIPassContents.SigningIdentity.AuthenticationType.password(_:)](jpkipasscontents/signingidentity-swift.struct/authenticationtype/password(_:).md)
  Reads the signing identity using the password.

## See Also

- [let signingIdentity: JPKIPassContents.SigningIdentity?](jpkipasscontents/signingidentity-swift.property.md)
  Allows access to the signing identity, if present in the JPKI applet.
- [func changePassword(from: String, to: String) async throws](jpkipasscontents/signingidentity-swift.struct/changepassword(from:to:).md)
  A function that allows you to change the password associated with the signing identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/signingidentity-swift.struct/authenticationtype)*