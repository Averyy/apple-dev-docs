# SecKeyImportExportParameters

**Framework**: Security  
**Kind**: struct

The legacy import/export parameter structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeyImportExportParameters
```

#### Overview

PKCS12 is an abbreviation for Public-Key Cryptography Standard # 12. This standard, by RSA Security, provides a format for external representation of keys and certificates and is described in .

## Topics

### Instance Properties
- [var accessRef: Unmanaged<SecAccess>?](seckeyimportexportparameters/accessref.md)
  Specifies the initial access controls of imported private keys.
- [var alertPrompt: Unmanaged<CFString>](seckeyimportexportparameters/alertprompt.md)
  The prompt to display in the secure passphrase alert panel.
- [var alertTitle: Unmanaged<CFString>](seckeyimportexportparameters/alerttitle.md)
  The title to display in the secure passphrase alert panel.
- [var flags: SecKeyImportExportFlags](seckeyimportexportparameters/flags.md)
  The bitwise `OR` of zero or more key import/export flags.
- [var keyAttributes: CSSM_KEYATTR_FLAGS](seckeyimportexportparameters/keyattributes.md)
  A word of bits constituting the low-level attribute flags for imported keys.
- [var keyUsage: CSSM_KEYUSE](seckeyimportexportparameters/keyusage.md)
  A word of bits constituting the low-level use flags for imported keys.
- [var passphrase: Unmanaged<CFTypeRef>?](seckeyimportexportparameters/passphrase.md)
  The password to use during key import or export.
- [var version: UInt32](seckeyimportexportparameters/version.md)
  The version of this structure.
### Initializers
- [init(version: UInt32, flags: SecKeyImportExportFlags, passphrase: Unmanaged<CFTypeRef>?, alertTitle: Unmanaged<CFString>, alertPrompt: Unmanaged<CFString>, accessRef: Unmanaged<SecAccess>?, keyUsage: CSSM_KEYUSE, keyAttributes: CSSM_KEYATTR_FLAGS)](seckeyimportexportparameters/init(version:flags:passphrase:alerttitle:alertprompt:accessref:keyusage:keyattributes:).md)
  Creates a new import/export parameter structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyimportexportparameters)*