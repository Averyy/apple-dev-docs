# Security

**Framework**: CKTool JS  
**Kind**: struct  
**Role**: Structure

A dictionary of your authorization tokens.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```
dictionary Security {
	string? CloudKitAPITokenAuth;
	string? CloudKitWebAuthTokenAuth;
	string? ManagementTokenAuth;
	string? UserTokenAuth;
};
```

## Overview

A dictionary that contains your management token, user token, or CloudKit tokens.

You pass this dictionary when creating an instance of a promises API class as one of its property values.

## Topics

### Instance Properties
- [CloudKitAPITokenAuth](./security/cloudkitapitokenauth.md)
  Your CloudKit API token.
- [CloudKitWebAuthTokenAuth](./security/cloudkitwebauthtokenauth.md)
  Your CloudKit Web Authentication token.
- [ManagementTokenAuth](./security/managementtokenauth.md)
  Your management token.
- [UserTokenAuth](./security/usertokenauth.md)
  Your user token.

## See Also

### Initialization
- [PromisesApi](./promisesapi/promisesapi.md)
  Creates a `PromisesApi` object.
- [PromisesApiOptions](./promisesapioptions.md)
  A dictionary of options for promises API classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/security)*