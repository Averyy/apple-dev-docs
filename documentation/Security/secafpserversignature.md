# SecAFPServerSignature

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

Represents a 16-byte Apple File Protocol server signature block.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

> **Deprecated**: Use internet password items instead of AppleShare password items.

## Declaration

```swift
typealias SecAFPServerSignature = (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

```c
typedef UInt8[16] SecAFPServerSignature;
```

#### Discussion

> ❗ **Important**:  This type is deprecated. Use internet password items instead of AppleShare password items.

This type represents a 16-byte Apple File Protocol server signature block. You can use a value of this type with the keychain item attribute constant [`SecItemAttr.signatureItemAttr`](./secitemattr/signatureitemattr.md) to specify an Apple File Protocol server signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secafpserversignature)*