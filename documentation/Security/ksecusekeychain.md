# kSecUseKeychain

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a keychain to operate on.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecUseKeychain: CFString
```

```c
extern CFStringRef const kSecUseKeychain;
```

#### Discussion

Specifies a [`SecKeychain`](./seckeychain.md) object that references the keychain to which [`SecItemAdd(_:_:)`](./secitemadd%28_,_%29.md) should add the provided items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecusekeychain)*