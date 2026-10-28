# kSecEncryptionMode

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The encryption mode.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecEncryptionMode: CFString
```

```c
extern CFStringRef const kSecEncryptionMode;
```

## Discussion

If you do not supply this key, an appropriate value will be supplied for you. See [Encryption Modes](./transform-attributes.md#Encryption-Modes) for a list of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecencryptionmode)*