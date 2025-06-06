# alertTitle

**Framework**: Security  
**Kind**: property

The title to display in the secure passphrase alert panel.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var alertTitle: Unmanaged<CFString>?
```

#### Discussion

When importing or exporting a key, if you set the [`securePassphrase`](seckeyimportexportflags/securepassphrase.md) flag bit, you can optionally use this field to specify a string for the password panel’s title bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/alerttitle)*