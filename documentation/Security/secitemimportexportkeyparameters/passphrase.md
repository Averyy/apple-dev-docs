# passphrase

**Framework**: Security  
**Kind**: property

The password to use during key import or export.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var passphrase: Unmanaged<CFTypeRef>?
```

#### Discussion

You may specify either a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) or a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) instance for the passphrase. The PKCS12 format requires passwords in Unicode format, and passing in a [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) as the password is the surest way to meet this requirement  (and ensure compatibility with other implementations). If you supply a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) instance as the password for a PKCS12 export operation, the data is assumed to be in UTF8 form and converted as appropriate.

When importing or exporting keys ([`SecKey`](seckey.md) objects) in one of the wrapped formats ([`SecExternalFormat.formatWrappedOpenSSL`](secexternalformat/formatwrappedopenssl.md), [`SecExternalFormat.formatWrappedSSH`](secexternalformat/formatwrappedssh.md), or [`SecExternalFormat.formatWrappedPKCS8`](secexternalformat/formatwrappedpkcs8.md)) or in PKCS12 format, you must either explicitly specify the passphrase field or set the [`securePassphrase`](seckeyimportexportflags/securepassphrase.md) bit the flags field (to prompt the user to enter the password).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/passphrase)*