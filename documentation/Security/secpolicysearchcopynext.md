# SecPolicySearchCopyNext

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves a policy object for the next policy matching specified search criteria.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecPolicySearchCopyNext(SecPolicySearchRef searchRef, SecPolicyRef*policyRef);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md). When there are no more policies that match the parameters specified to [`SecPolicySearchCreate`](./secpolicysearchcreate.md), [`errSecPolicyNotFound`](./errsecpolicynotfound.md) is returned.

## Parameters

- `searchRef`: A policy search object specifying the search criteria for this search. You create the policy search object by calling the [`SecPolicySearchCreate`](./secpolicysearchcreate.md) function.
- `policyRef`: On return, points to the policy object for the next policy (if any) matching the specified search criteria. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicysearchcopynext)*