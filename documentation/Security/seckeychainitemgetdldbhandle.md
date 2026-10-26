# SecKeychainItemGetDLDBHandle

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the CSSM database handle for a given keychain item object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: The common security services manager module is no longer used.

## Declaration

```c
OSStatus SecKeychainItemGetDLDBHandle(SecKeychainItemRef keyItemRef, CSSM_DL_DB_HANDLE *dldbHandle);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

> ❗ **Important**:  This function is deprecated. The common security services manager module is no longer used.

## Parameters

- `keyItemRef`: A keychain item object.
- `dldbHandle`: On return, a pointer to a CSSM database handle for the keychain database containing the given item. The handle is valid until the keychain item object is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemgetdldbhandle)*