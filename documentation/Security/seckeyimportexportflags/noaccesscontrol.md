# noAccessControl

**Framework**: Security  
**Kind**: property

A flag that indicates imported private keys have no access object attached to them.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static var noAccessControl: SecKeyImportExportFlags { get }
```

#### Discussion

In the absence of both this bit and the [`accessRef`](secitemimportexportkeyparameters/accessref.md) field in the [`SecItemImportExportKeyParameters`](secitemimportexportkeyparameters.md) structure, imported private keys receive default access controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyimportexportflags/noaccesscontrol)*