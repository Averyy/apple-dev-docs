# alertPrompt

**Framework**: Security  
**Kind**: property

The prompt to display in the secure passphrase alert panel.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var alertPrompt: Unmanaged<CFString>
```

#### Discussion

When importing or exporting a key, if you set the [`securePassphrase`](seckeyimportexportflags/securepassphrase.md) flag bit, you can optionally use this field to specify a string for the prompt that appears in the password panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyimportexportparameters/alertprompt)*