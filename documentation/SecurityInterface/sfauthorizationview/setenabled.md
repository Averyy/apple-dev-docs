# setEnabled(_:)

**Framework**: Security Interface  
**Kind**: method

Sets the current state of the authorization view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func setEnabled(_ enabled: Bool)
```

#### Discussion

A disabled view is visible but dimmed.

## Parameters

- `enabled`: Specifies whether the authorization view should be enabled ( ) or disabled ( ).

## Topics

### Related Documentation
- [func authorizationState() -> SFAuthorizationViewState](sfauthorizationview/authorizationstate.md)
  Returns the current state of the authorization view.

## See Also

- [func setString(AuthorizationString!)](sfauthorizationview/setstring(_:).md)
  Sets the requested-right string to use with the default authorization rights set.
- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](sfauthorizationview/setauthorizationrights(_:).md)
  Sets the authorization rights for this view.
- [func setAutoupdate(Bool)](sfauthorizationview/setautoupdate(_:).md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](sfauthorizationview/setautoupdate(_:interval:).md)
  Sets the authorization view to update itself at a specific interval.
- [func setFlags(AuthorizationFlags)](sfauthorizationview/setflags(_:).md)
  Sets the current authorization flags for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setenabled(_:))*