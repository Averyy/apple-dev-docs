# setPassword(_:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method

Sets the password from the supplied string.

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
func setPassword(_ password: String) throws
```

#### Discussion

Use this function to encrypt or decrypt an archive with the [`scrypt`](./encryptionmode-swift.struct/scrypt.md) encryption mode.

## Parameters

- `password`: The password.

## See Also

### Setting a password
- [var password: String?](./password.md)
  The password used to encrypt or decrypt an archive.
- [func generatePassword() throws -> String](./generatepassword%28%29.md)
  Generates a new password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/setpassword(_:))*