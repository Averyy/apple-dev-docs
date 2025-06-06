# keyAttributes

**Framework**: Security  
**Kind**: property

A word of bits constituting the low-level attribute flags for imported keys.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var keyAttributes: CSSM_KEYATTR_FLAGS
```

#### Discussion

The default value is `CSSM_KEYATTR_SENSITIVE` `|` `CSSM_KEYATTR_EXTRACTABLE`; the `CSSM_KEYATTR_PERMANENT` bit is also added to the default if a non-NULL value is specified for the `importKeychain` parameter.

The following are valid values for these flags: `CSSM_KEYATTR_PERMANENT`, `CSSM_KEYATTR_SENSITIVE`, and `CSSM_KEYATTR_EXTRACTABLE`.

If the `CSSM_KEYATTR_PERMANENT` bit is set, the `importKeychain` parameter is not valid, and if any keys are found in the external representation, then the error [`errSecInvalidKeychain`](errsecinvalidkeychain.md) is returned.

The `CSSM_KEYATTR_SENSITIVE` bit indicates that the key can only be extracted in wrapped form.

> ❗ **Important**:  If you do not set the `CSSM_KEYATTR_EXTRACTABLE` bit, you cannot extract the imported key from the keychain in any form, including in wrapped form.

 If you do not set the `CSSM_KEYATTR_EXTRACTABLE` bit, you cannot extract the imported key from the keychain in any form, including in wrapped form.

The `CSSM_KEYATTR_FLAGS` enumeration is defined in `cssmtype.h`. Note that the `CSSM_KEYATTR_RETURN_xxx` bits are always forced to `CSSM_KEYATTR_RETURN_REF` regardless of how they are specified in the `keyAttributes` field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyimportexportparameters/keyattributes)*