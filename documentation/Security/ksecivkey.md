# kSecIVKey

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The setting for an initialization vector.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecIVKey: CFString
```

```c
extern CFStringRef const kSecIVKey;
```

#### Discussion

The key’s associated value is an initialization vector. Provide random bytes for this value—for example, created by calling the [`SecRandomCopyBytes(_:_:_:)`](./secrandomcopybytes%28_,_,_%29.md) method—unless your specification requires something else. The number of bytes in the vector should match the block size of the underlying block cipher. For example, use 16 bytes for AES encryption.

If you don’t supply a value for this key, any operations that require an initialization vector use a value of zero by default, which can compromise the security of your encryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecivkey)*