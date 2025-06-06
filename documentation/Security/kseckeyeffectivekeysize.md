# kSecKeyEffectiveKeySize

**Framework**: Security  
**Kind**: var

Type uint32; value is the effective number of bits in this key.  For example, a DES key has a key size in bits (`kSecKeyKeySizeInBits`) of 64 but a value for `kSecKeyEffectiveKeySize` of 56.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var kSecKeyEffectiveKeySize: Int32 { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseckeyeffectivekeysize)*