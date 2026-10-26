# SecPolicySetProperties

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets properties for a policy.

**Availability**:
- macOS 10.7+ - Deprecated in 10.9

## Declaration

```c
OSStatus SecPolicySetProperties(SecPolicyRef policyRef, CFDictionaryRef properties);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Parameters

- `policyRef`: The policy to alter
- `properties`: A `CFDictionaryRef` object containing the new set of properties. For a list of valid property keys, see [Security Policy Keys](./security-policy-keys.md).

  > **Note**:  The property [`kSecPolicyOid`](./ksecpolicyoid.md) is read-only and thus cannot be changed by this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicysetproperties)*