# keyUsage

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

An array containing usage attributes applied to a key on import.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var keyUsage: Unmanaged<CFArray>?
```

```c
CFArrayRef keyUsage;
```

#### Discussion

The array may contain any of the following key usage constants:

- [`kSecAttrCanEncrypt`](../ksecattrcanencrypt.md)
- [`kSecAttrCanDecrypt`](../ksecattrcandecrypt.md)
- [`kSecAttrCanDerive`](../ksecattrcanderive.md)
- [`kSecAttrCanSign`](../ksecattrcansign.md)
- [`kSecAttrCanVerify`](../ksecattrcanverify.md)
- [`kSecAttrCanWrap`](../ksecattrcanwrap.md)
- [`kSecAttrCanUnwrap`](../ksecattrcanunwrap.md)

If the array is `NULL`, all operations are allowed by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/keyusage)*