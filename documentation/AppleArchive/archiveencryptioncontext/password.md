# password

**Framework**: Apple Archive  
**Kind**: property  
**Role**: Instance Property

The password used to encrypt or decrypt an archive.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
var password: String? { get set }
```

#### Discussion

Use the [`generatePassword()`](./generatepassword%28%29.md) function to generate random high entropy passwords.

## See Also

### Setting a password
- [func generatePassword() throws -> String](./generatepassword%28%29.md)
  Generates a new password.
- [func setPassword(String) throws](./setpassword%28_%29.md)
  Sets the password from the supplied string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/password)*