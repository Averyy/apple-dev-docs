# accessRef

**Framework**: Security  
**Kind**: property

Specifies the initial access controls of imported private keys.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var accessRef: Unmanaged<SecAccess>?
```

#### Discussion

If more than one private key is being imported, all private keys get the same initial access controls. If this field is `NULL` when private keys are being imported, then the access object for the keychain item for an imported private key depends on the [`noAccessControl`](seckeyimportexportflags/noaccesscontrol.md) bit in the `flags` parameter. When that flag is `0` (or `keyParams` is `NULL`), the default access control is used. When the flag is `1`, no access object is attached to the keychain item for imported private keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/accessref)*