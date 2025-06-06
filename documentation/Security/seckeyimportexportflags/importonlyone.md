# importOnlyOne

**Framework**: Security  
**Kind**: property

A flag that you set to prevent importing more than one private key.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static var importOnlyOne: SecKeyImportExportFlags { get }
```

#### Discussion

Prevents the importing of more than one private key by the [`SecKeychainItemImport`](seckeychainitemimport.md) function. If the `importKeychain` parameter is `NULL`, this bit is ignored. Otherwise, if this bit is set and there is more than one key in the incoming external representation, no items are imported to the specified keychain and the error `errSecMultipleKeys` is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyimportexportflags/importonlyone)*