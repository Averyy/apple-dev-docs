# kSecInputIsRaw

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The input is raw.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecInputIsRaw: CFString
```

```c
extern CFStringRef const kSecInputIsRaw;
```

#### Discussion

Using this type of input can be cryptographically unsafe (for example if you don’t blind a DSA or ECDSA signature you give away the key very quickly). You are strongly discouraged from using it..


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecinputisraw)*