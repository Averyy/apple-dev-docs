# SecKeychainGetDLDBHandle

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the CSSM database handle for a given keychain object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: The common security services manager module is no longer used.

## Declaration

```c
OSStatus SecKeychainGetDLDBHandle(SecKeychainRef keychain, CSSM_DL_DB_HANDLE *dldbHandle);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

> ❗ **Important**:  This function is deprecated. The common security services manager module is no longer used.

## Parameters

- `keychain`: A keychain object.
- `dldbHandle`: On return, a pointer to the CSSM database handle for the given keychain. The handle is valid until the keychain object is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaingetdldbhandle)*