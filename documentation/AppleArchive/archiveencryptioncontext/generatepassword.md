# generatePassword()

**Framework**: Apple Archive  
**Kind**: method

Generates a new password.

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
func generatePassword() throws -> String
```

#### Return Value

The new password.

#### Discussion

This function generates a new high entropy password, stores it in the context, and returns it.

## See Also

- [var password: String?](archiveencryptioncontext/password.md)
  The password used to encrypt or decrypt an archive.
- [func setPassword(String) throws](archiveencryptioncontext/setpassword(_:).md)
  Sets the password from the supplied string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/generatepassword())*