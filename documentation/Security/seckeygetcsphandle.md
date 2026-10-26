# SecKeyGetCSPHandle

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the CSSM CSP handle for a key.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecKeyGetCSPHandle(SecKeyRef keyRef, CSSM_CSP_HANDLE *cspHandle);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

A CSSM CSP handle is required as an input to a number of CSSM functions.

## Parameters

- `keyRef`: The key for which you want a CSSM CSP handle.
- `cspHandle`: On return, points to the CSSM CSP handle for the specified key. This pointer remains valid until the key reference is released. Do not attempt to modify or free this data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygetcsphandle)*