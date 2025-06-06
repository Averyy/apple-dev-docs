# setPassword(_:)

**Framework**: Apple Archive  
**Kind**: method

Sets the password from the supplied string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func setPassword(_ password: String) throws
```

#### Discussion

Use this function to encrypt or decrypt an archive with the [`scrypt`](archiveencryptioncontext/encryptionmode-swift.struct/scrypt.md) encryption mode.

## Parameters

- `password`: The password.

## See Also

- [var password: String?](archiveencryptioncontext/password.md)
  The password used to encrypt or decrypt an archive.
- [func generatePassword() throws -> String](archiveencryptioncontext/generatepassword.md)
  Generates a new password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/setpassword(_:))*