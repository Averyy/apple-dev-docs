# kSecAttrSalt

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the salt to use for this item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecAttrSalt: CFString
```

```c
extern CFStringRef const kSecAttrSalt;
```

#### Discussion

The corresponding value is of type [`CFData`](../CoreFoundation/cfdata.md) that indicates the salt to use with this cryptographic key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrsalt)*