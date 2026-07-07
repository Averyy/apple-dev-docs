# changePassword(from:to:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

A function that allows you to change the password associated with the signing identity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func changePassword(from oldValue: String, to newValue: String) async throws
```

## Parameters

- `oldValue`: The user authentication value used to perform the request to change the password.
- `newValue`: The new user authentication value applied to the signing identity.

## See Also

- [let signingIdentity: JPKIPassContents.SigningIdentity?](jpkipasscontents/signingidentity-swift.property.md)
  Allows access to the signing identity, if present in the JPKI applet.
- [JPKIPassContents.SigningIdentity.AuthenticationType](jpkipasscontents/signingidentity-swift.struct/authenticationtype.md)
  Defines the valid user authentication request options for the signing identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/signingidentity-swift.struct/changepassword(from:to:))*