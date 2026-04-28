# UserNameAndPasswordCredential

**Framework**: Device Management  
**Kind**: dictionary

Data that describes a credential that represents a user name and password.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object UserNameAndPasswordCredential
```

## Properties

- `Password` (string): The password for this credential.
- `UserName` (string) *(required)*: The user name for this credential.

## See Also

- [object ACMECredential](acmecredential.md)
  An ACME identity that the device generates.
- [object IdentityCredential](identitycredential.md)
  The data for a PKCS #12 password-protected identity.
- [object SCEPCredential](scepcredential.md)
  A SCEP identity that the device generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/usernameandpasswordcredential)*