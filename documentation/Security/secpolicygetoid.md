# SecPolicyGetOID

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves a policy’s object identifier.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecPolicyGetOID(SecPolicyRef policyRef, SecAsn1Oid *oid);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

The policy’s object identifier, in the form of a `CSSM_OID` structure, is used in the CSSM API together with the policy’s value. Use the [`SecPolicyGetValue`](./secpolicygetvalue.md) function to obtain the value that corresponds to this object identifier.

## Parameters

- `policyRef`: The policy object for which to obtain the object identifier. You can obtain a policy object with the [`SecPolicySearchCopyNext`](./secpolicysearchcopynext.md) function.
- `oid`: On return, points to the policy’s object identifier. This identifier is owned by the policy object and remains valid until that object is destroyed; do not release it separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicygetoid)*