# init(version:flags:passphrase:alertTitle:alertPrompt:accessRef:keyUsage:keyAttributes:)

**Framework**: Security  
**Kind**: init

Creates a new import/export parameter structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init(version: UInt32, flags: SecKeyImportExportFlags, passphrase: Unmanaged<CFTypeRef>?, alertTitle: Unmanaged<CFString>, alertPrompt: Unmanaged<CFString>, accessRef: Unmanaged<SecAccess>?, keyUsage: CSSM_KEYUSE, keyAttributes: CSSM_KEYATTR_FLAGS)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyimportexportparameters/init(version:flags:passphrase:alerttitle:alertprompt:accessref:keyusage:keyattributes:))*