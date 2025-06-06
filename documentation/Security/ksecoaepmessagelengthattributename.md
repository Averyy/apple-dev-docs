# kSecOAEPMessageLengthAttributeName

**Framework**: Security  
**Kind**: var

The OAEP message length.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecOAEPMessageLengthAttributeName: CFString
```

#### Discussion

Optionally set the value to a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) indicating a specific message size when the [`kSecPaddingKey`](ksecpaddingkey.md) attribute is set to [`kSecPaddingOAEPKey`](ksecpaddingoaepkey.md). If you don’t set this attribute, the minimum padding is used by default.

This attribute is ignored when padding is not set to OAEP.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecoaepmessagelengthattributename)*