# kSecIVKey

**Framework**: Security  
**Kind**: var

The setting for an initialization vector.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecIVKey: CFString
```

#### Discussion

The key’s associated value is an initialization vector. Provide random bytes for this value—for example, created by calling the [`SecRandomCopyBytes(_:_:_:)`](secrandomcopybytes(_:_:_:).md) method—unless your specification requires something else. The number of bytes in the vector should match the block size of the underlying block cipher. For example, use 16 bytes for AES encryption.

If you don’t supply a value for this key, any operations that require an initialization vector use a value of zero by default, which can compromise the security of your encryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecivkey)*