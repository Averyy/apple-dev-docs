# kSecACLAuthorizationImportWrapped

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

Import an encrypted key. This tag is checked on the key being imported; in addition, the `CSSM_ACL_AUTHORIZATION_DECRYPT` tag is checked for any key used in the unwrapping operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecACLAuthorizationImportWrapped: CFString
```

```c
extern CFStringRef const kSecACLAuthorizationImportWrapped;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecaclauthorizationimportwrapped)*