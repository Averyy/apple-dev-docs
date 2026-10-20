# SecItemAttr.signatureItemAttr

**Framework**: Security  
**Kind**: case  
**Role**: Case

Identifies the server signature attribute.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case signatureItemAttr
```

```c
kSecSignatureItemAttr
```

#### Discussion

You use this tag to set or get a value of type [`SecAFPServerSignature`](../secafpserversignature.md) that represents the server signature block. This is unique to AppleShare password attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemattr/signatureitemattr)*