# SecKeychainGetCSPHandle

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the CSSM CSP handle for the given keychain object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: The common security services manager module is no longer used.

## Declaration

```c
OSStatus SecKeychainGetCSPHandle(SecKeychainRef keychain, CSSM_CSP_HANDLE *cspHandle);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

> ❗ **Important**:  This function is deprecated. The common security services manager module is no longer used.

## Parameters

- `keychain`: A keychain object.
- `cspHandle`: On return, a pointer to the CSSM CSP handle for the given keychain. The handle is valid until the keychain object is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaingetcsphandle)*