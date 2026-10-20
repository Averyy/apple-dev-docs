# JPKIPassContents.SigningIdentity.AuthenticationType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

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
- [JPKIPassContents.SigningIdentity.AuthenticationType.password(_:)](./authenticationtype/password%28_%29.md)
  Reads the signing identity using the password.

## See Also

### Signing identity authentication
- [let signingIdentity: JPKIPassContents.SigningIdentity?](../signingidentity-swift.property.md)
  Allows access to the signing identity, if present in the JPKI applet.
- [func changePassword(from: String, to: String) async throws](./changepassword%28from,to%29.md)
  A function that allows you to change the password associated with the signing identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/signingidentity-swift.struct/authenticationtype)*