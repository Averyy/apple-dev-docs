# SecPolicySearchCreate

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a search object for finding policies.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecPolicySearchCreate(CSSM_CERT_TYPE certType, const SecAsn1Oid *policyOID, const SecAsn1Item *value, SecPolicySearchRef*searchRef);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

You use the search object created by this function in subsequent calls to the [`SecPolicySearchCopyNext`](./secpolicysearchcopynext.md) function to obtain trust policy objects. Policies are stored in the Module Directory Services (MDS) database. MDS is described in detail in “Part 8: Module Directory Service (MDS)” of *Common Security: CDSA and CSSM, version 2 (with corrigenda)* from The Open Group ([http://www.opengroup.org/security/cdsa.htm](http://www.opengroup.org/security/cdsa.htm)).

## Parameters

- `certType`: The type of certificates a policy uses, as defined in `Security.framework/cssmtype.h`. Permissible values are `CSSM_CERT_X_509v1`, `CSSM_CERT_X_509v2`, and `CSSM_CERT_X_509v3`. If you are unsure of the certificate type, use `CSSM_CERT_X_509v3`.
- `policyOID`: A pointer to a BER-encoded policy object identifier that uniquely specifies the policy. See [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md) for a list of policies and object identifiers provided by the AppleX509TP module.
- `value`: A pointer to an optional, policy-defined value. The contents of this value depend on the policy object identifier specified. (Note that this parameter refers to the value stored in MDS and is not related to the `value` parameter of the [`SecPolicyGetValue`](./secpolicygetvalue.md) function.) Currently the function does not use this parameter; pass `NULL` for this pointer.
- `searchRef`: On return, points to the newly created policy search object. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicysearchcreate)*