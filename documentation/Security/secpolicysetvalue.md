# SecPolicySetValue

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets a policy’s value.

**Availability**:
- macOS 10.2+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecPolicySetValue(SecPolicyRef policyRef, const SecAsn1Item *value);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

A policy’s value is defined and interpreted by the policy. If you are using CSSM, you can specify object-identifier–policy-value pairs as input to the `CSSM_TP_POLICYINFO` function. Use the [`SecPolicyGetOID`](./secpolicygetoid.md) function to obtain the object identifier (OID) for a policy.

Depending on how the policy uses the value, the value can be specific to a transaction. Because some other process might be using this policy object, it is best not to assign a new value to the policy using the same policy object. Instead, obtain a new policy object before assigning a new value to the policy.

## Parameters

- `policyRef`: The policy object whose value you wish to set.
- `value`: The value to be set into the policy object, replacing any previous value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicysetvalue)*