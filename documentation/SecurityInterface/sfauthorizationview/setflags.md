# setFlags(_:)

**Framework**: Security Interface  
**Kind**: method

Sets the current authorization flags for the view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func setFlags(_ flags: AuthorizationFlags)
```

#### Discussion

You can use this method to change the authorization flag settings made with the [`setAuthorizationRights(_:)`](sfauthorizationview/setauthorizationrights(_:).md) method or to specify flags other than the default ([`kAuthorizationFlagDefaults`](https://developer.apple.com/documentation/Security/AuthorizationFlags/kAuthorizationFlagDefaults)) used by the [`setString(_:)`](sfauthorizationview/setstring(_:).md) method.

The authorization flags are described in Authorization Options in [`Authorization Services`](https://developer.apple.com/documentation/Security/authorization-services).

## Parameters

- `flags`: The authorization flags to set for this view.

## See Also

- [func setString(AuthorizationString!)](sfauthorizationview/setstring(_:).md)
  Sets the requested-right string to use with the default authorization rights set.
- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](sfauthorizationview/setauthorizationrights(_:).md)
  Sets the authorization rights for this view.
- [func setAutoupdate(Bool)](sfauthorizationview/setautoupdate(_:).md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](sfauthorizationview/setautoupdate(_:interval:).md)
  Sets the authorization view to update itself at a specific interval.
- [func setEnabled(Bool)](sfauthorizationview/setenabled(_:).md)
  Sets the current state of the authorization view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setflags(_:))*