# useClassicalSignature

**Framework**: Security  
**Kind**: property

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
static var useClassicalSignature: SecCSFlags { get }
```

#### Discussion

When passed to a validation or inspection call on a dual-signed code object, select the classical (RSA) signature slot for validation and information retrieval. Mutually exclusive with kSecCSUsePostQuantumSignature; passing both returns errSecCSInvalidFlags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccsflags/useclassicalsignature)*