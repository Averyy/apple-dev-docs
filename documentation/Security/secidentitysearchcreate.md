# SecIdentitySearchCreate

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates a search object for finding identities.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecIdentitySearchCreate(CFTypeRef keychainOrArray, CSSM_KEYUSE keyUsage, SecIdentitySearchRef*searchRef);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

You can OR `CSSM_KEYUSE` values together to set more than one value for key use. Use the returned search object in calls to the [`SecIdentitySearchCopyNext`](./secidentitysearchcopynext.md) function to obtain identities that match the search criteria.

## Parameters

- `keychainOrArray`: A keychain object for a single keychain to search, an array of keychain objects for a set of keychains to search, or `NULL` to search the user’s default keychain search list.
- `keyUsage`: A CSSM key use value as defined in `Security.framework/cssmtype.h`. (Note that, because key recovery is not implemented, the `SIGN_RECOVER` and `VERIFY_RECOVER` constants are not supported.) Use this parameter to filter the search by specifying the key use for the identity. Pass `0` if you want all identities returned by this search. Pass `CSSM_KEYUSE_ANY` to limit the identities returned to those that can be used for every operation.
- `searchRef`: On return, points to the identity search object. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are done with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitysearchcreate)*