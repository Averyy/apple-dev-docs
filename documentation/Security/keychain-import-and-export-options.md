# Keychain Import and Export Options

**Framework**: Security

Use these constants when you pass dictionary-based arguments to import and export functions.

## Topics

### Constants
- [let kSecImportExportPassphrase: CFString](ksecimportexportpassphrase.md)
  A passphrase (represented by a `CFStringRef` object) to be used when exporting to or importing from PKCS#12 format.
- [let kSecImportExportKeychain: CFString](ksecimportexportkeychain.md)
  A keychain represented by a SecKeychainRef to be used as the target when importing or exporting.
- [let kSecImportExportAccess: CFString](ksecimportexportaccess.md)
  An initial access control list represented by a [`SecAccess`](secaccess.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/keychain-import-and-export-options)*