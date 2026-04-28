# PasswordHash

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains the password hash for the account.

**Availability**:
- macOS 10.11+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object PasswordHash
```

## Topics

### Objects
- [object PasswordHash.SALTED-SHA512-PBKDF2](passwordhash/salted-sha512-pbkdf2-data.dictionary.md)
  A dictionary that contains the elements to create the password hash.

## Properties

- `SALTED-SHA512-PBKDF2` (PasswordHash.SALTED-SHA512-PBKDF2) *(required)*: A dictionary that contains the `entropy`, `iterations`, and `salt` elements to create the password hash using the CommonCrypto libraries, or equivalent. Convert this dictionary to binary data before setting it as the value for the password hash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/passwordhash)*