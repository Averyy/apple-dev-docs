# keyAttributes

**Framework**: Security  
**Kind**: property

An array containing zero or more key attributes for an imported key.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var keyAttributes: Unmanaged<CFArray>?
```

#### Discussion

Valid values are [`kSecAttrIsPermanent`](ksecattrispermanent.md), [`kSecAttrIsSensitive`](ksecattrissensitive.md), and [`kSecAttrIsExtractable`](ksecattrisextractable.md). If you set this attribute array to `NULL`, the following defaults are used:

- The item is marked permanent if a keychain is specified.
- The item is marked sensitive if it is a private key.
- The item is marked extractable by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/keyattributes)*