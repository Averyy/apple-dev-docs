# kSecImportItemKeyID

**Framework**: Security  
**Kind**: var

Key ID.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecImportItemKeyID: CFString
```

## Mentions

- [Importing an Identity](importing-an-identity.md)

#### Discussion

The corresponding value is of type `CFDataRef`. This unique ID is often the SHA-1 digest of the public encryption key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecimportitemkeyid)*