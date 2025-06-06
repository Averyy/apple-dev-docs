# pemArmour

**Framework**: Security  
**Kind**: property

A flag that indicates the exported data should have PEM armor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static var pemArmour: SecItemImportExportFlags { get }
```

#### Discussion

PEM armor refers to a way of expressing binary data as an ASCII string so that it can be transferred over text-only channels such as email. (PEM stands for an Internet standard, Privacy Enhanced Mail.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimportexportflags/pemarmour)*