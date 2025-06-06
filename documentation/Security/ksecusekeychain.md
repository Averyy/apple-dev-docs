# kSecUseKeychain

**Framework**: Security  
**Kind**: var

A key whose value is a keychain to operate on.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecUseKeychain: CFString
```

#### Discussion

Specifies a [`SecKeychain`](seckeychain.md) object that references the keychain to which [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) should add the provided items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecusekeychain)*