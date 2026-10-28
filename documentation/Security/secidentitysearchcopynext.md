# SecIdentitySearchCopyNext

**Framework**: Security  
**Kind**: func  
**Role**: Function

Finds the next identity matching specified search criteria

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecIdentitySearchCopyNext(SecIdentitySearchRef searchRef, SecIdentityRef*identity);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md). When there are no more identities that match the parameters specified to [`SecIdentitySearchCreate`](./secidentitysearchcreate.md), [`errSecItemNotFound`](./errsecitemnotfound.md) is returned.

## Parameters

- `searchRef`: An identity search object specifying the search criteria for this search. You create the identity search object by calling the [`SecIdentitySearchCreate`](./secidentitysearchcreate.md) function.
- `identity`: On return, points to the identity object of the next matching identity (if any). In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitysearchcopynext)*