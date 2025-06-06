# Authorization Rights Flags

**Framework**: Security

Recognize the values the Security Server sets in an authorization item’s flag field.

#### Overview

Look for these values in the [`flags`](authorizationitem/flags.md) field of an [`AuthorizationItem`](authorizationitem.md), for example among the set of items in the `authorizedRights` parameter returned by a call to the [`AuthorizationCopyInfo(_:_:_:)`](authorizationcopyinfo(_:_:_:).md) function.

## Topics

### Constants
- [var kAuthorizationFlagCanNotPreAuthorize: Int](kauthorizationflagcannotpreauthorize.md)
  Indicates the Security Server could not preauthorizethe right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorization-rights-flags)*