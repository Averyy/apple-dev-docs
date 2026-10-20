# kSecACLAuthorizationExportWrapped

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

Export a wrapped (that is, encrypted) key. This tag is checked on the key being exported; in addition, the `CSSM_ACL_AUTHORIZATION_ENCRYPT` tag is checked for any key used in the wrapping operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecACLAuthorizationExportWrapped: CFString
```

```c
extern CFStringRef const kSecACLAuthorizationExportWrapped;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecaclauthorizationexportwrapped)*