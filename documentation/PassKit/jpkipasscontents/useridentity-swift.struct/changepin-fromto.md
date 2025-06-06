# changePIN(from:to:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

A function that allows for the change of the PIN associated with the user identity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func changePIN(from oldValue: String, to newValue: String) async throws
```

## Parameters

- `oldValue`: The user authentication value used to perform the request to change the PIN.
- `newValue`: The new user authentication value applied to user identity.

## See Also

- [let userIdentity: JPKIPassContents.UserIdentity?](jpkipasscontents/useridentity-swift.property.md)
  Allows for access to the user identity, if present in the JPKI applet.
- [JPKIPassContents.UserIdentity.AuthenticationType](jpkipasscontents/useridentity-swift.struct/authenticationtype.md)
  Defines valid authentication types associated with the user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/useridentity-swift.struct/changepin(from:to:))*