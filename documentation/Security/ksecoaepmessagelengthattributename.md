# kSecOAEPMessageLengthAttributeName

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The OAEP message length.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecOAEPMessageLengthAttributeName: CFString
```

```c
extern CFStringRef const kSecOAEPMessageLengthAttributeName;
```

## Discussion

Optionally set the value to a [`CFNumber`](../CoreFoundation/cfnumber.md) indicating a specific message size when the [`kSecPaddingKey`](./ksecpaddingkey.md) attribute is set to [`kSecPaddingOAEPKey`](./ksecpaddingoaepkey.md). If you don’t set this attribute, the minimum padding is used by default.

This attribute is ignored when padding is not set to OAEP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecoaepmessagelengthattributename)*