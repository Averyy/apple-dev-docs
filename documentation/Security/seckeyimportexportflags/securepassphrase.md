# securePassphrase

**Framework**: Security  
**Kind**: property

A flag that indicates the user should be prompted for a passphrase on import or export.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static var securePassphrase: SecKeyImportExportFlags { get }
```

#### Discussion

When set, the password for import or export is obtained by user prompt. (A password is sometimes referred to as a passphrase to emphasize the fact that a longer string that includes non-letter characters, such as numbers, punctuation, and spaces, is more secure than a simple word.) Otherwise, you must provide the password in the [`passphrase`](secitemimportexportkeyparameters/passphrase.md) field of the [`SecItemImportExportKeyParameters`](secitemimportexportkeyparameters.md) structure. A user-supplied password is preferred, because it avoids having the cleartext password appear in the application’s address space at any time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyimportexportflags/securepassphrase)*