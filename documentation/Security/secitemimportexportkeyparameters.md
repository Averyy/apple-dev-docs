# SecItemImportExportKeyParameters

**Framework**: Security  
**Kind**: struct

The import/export parameter structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecItemImportExportKeyParameters
```

#### Overview

Use this structure as the `keyParams` input parameter to the [`SecItemExport(_:_:_:_:_:)`](secitemexport(_:_:_:_:_:).md) and the [`SecItemImport(_:_:_:_:_:_:_:_:)`](secitemimport(_:_:_:_:_:_:_:_:).md) functions.

## Topics

### Instance Properties
- [var accessRef: Unmanaged<SecAccess>?](secitemimportexportkeyparameters/accessref.md)
  Specifies the initial access controls of imported private keys.
- [var alertPrompt: Unmanaged<CFString>?](secitemimportexportkeyparameters/alertprompt.md)
  The prompt to display in the secure passphrase alert panel.
- [var alertTitle: Unmanaged<CFString>?](secitemimportexportkeyparameters/alerttitle.md)
  The title to display in the secure passphrase alert panel.
- [var flags: SecKeyImportExportFlags](secitemimportexportkeyparameters/flags.md)
  The bitwise `OR` of zero or more key import/export flags.
- [var keyAttributes: Unmanaged<CFArray>?](secitemimportexportkeyparameters/keyattributes.md)
  An array containing zero or more key attributes for an imported key.
- [var keyUsage: Unmanaged<CFArray>?](secitemimportexportkeyparameters/keyusage.md)
  An array containing usage attributes applied to a key on import.
- [var passphrase: Unmanaged<CFTypeRef>?](secitemimportexportkeyparameters/passphrase.md)
  The password to use during key import or export.
- [var version: UInt32](secitemimportexportkeyparameters/version.md)
  The version of this structure.
### Initializers
- [init()](secitemimportexportkeyparameters/init.md)
- [init(version: UInt32, flags: SecKeyImportExportFlags, passphrase: Unmanaged<CFTypeRef>?, alertTitle: Unmanaged<CFString>?, alertPrompt: Unmanaged<CFString>?, accessRef: Unmanaged<SecAccess>?, keyUsage: Unmanaged<CFArray>?, keyAttributes: Unmanaged<CFArray>?)](secitemimportexportkeyparameters/init(version:flags:passphrase:alerttitle:alertprompt:accessref:keyusage:keyattributes:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters)*