# usePostQuantumSignature

**Framework**: Security  
**Kind**: property

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
static var usePostQuantumSignature: SecCSFlags { get }
```

#### Discussion

When passed to a validation or inspection call on a dual-signed code object, select the post-quantum (PQ) signature slot for validation and information retrieval. Mutually exclusive with kSecCSUseClassicalSignature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccsflags/usepostquantumsignature)*