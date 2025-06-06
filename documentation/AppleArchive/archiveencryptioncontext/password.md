# password

**Framework**: Apple Archive  
**Kind**: property

The password used to encrypt or decrypt an archive.

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
var password: String? { get set }
```

#### Discussion

Use the [`generatePassword()`](archiveencryptioncontext/generatepassword().md) function to generate random high entropy passwords.

## See Also

- [func generatePassword() throws -> String](archiveencryptioncontext/generatepassword.md)
  Generates a new password.
- [func setPassword(String) throws](archiveencryptioncontext/setpassword(_:).md)
  Sets the password from the supplied string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/password)*