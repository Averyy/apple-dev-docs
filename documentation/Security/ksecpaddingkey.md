# kSecPaddingKey

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The kind of padding to use.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecPaddingKey: CFString
```

```c
extern CFStringRef const kSecPaddingKey;
```

## Discussion

If you do not supply a value for this key, an appropriate value will be supplied for you. See [Padding Types](./transform-attributes.md#Padding-Types) for a list of valid values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecpaddingkey)*