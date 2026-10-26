# SecPolicyGetTPHandle

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves the trust policy handle for a policy object.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecPolicyGetTPHandle(SecPolicyRef policyRef, CSSM_TP_HANDLE *tpHandle);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

The trust policy handle is the CSSM identifier of the trust policy module that is managing the certificate. The trust policy handle is uses as an input to a number of CSSM functions.

## Parameters

- `policyRef`: The policy object from which to obtain the trust policy handle.
- `tpHandle`: On return, points to the policy object’s trust policy handle. The handle remains valid until the policy object is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicygettphandle)*