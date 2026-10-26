# AuthorizationContextFlags

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The flags that specify whether authentication data should be made available to the authorization client.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
enum AuthorizationContextFlags : UInt32;
```

## Topics

### Constants
- [kAuthorizationContextFlagExtractable](./authorizationcontextflags/kauthorizationcontextflagextractable.md)
  It is possible for the authorization client to use the [`AuthorizationCopyInfo(_:_:_:)`](./authorizationcopyinfo%28_,_,_%29.md) function to obtain the value.
- [kAuthorizationContextFlagVolatile](./authorizationcontextflags/kauthorizationcontextflagvolatile.md)
  The value is not saved for the authorization client.
- [kAuthorizationContextFlagSticky](./authorizationcontextflags/kauthorizationcontextflagsticky.md)
  This data persists through an interrupted or failed evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcontextflags)*