# setString(_:)

**Framework**: Security Interface  
**Kind**: method

Sets the requested-right string to use with the default authorization rights set.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func setString(_ authorizationString: AuthorizationString!)
```

#### Discussion

This is a convenience method that creates an authorization rights set when you specify only the name of the requested right. The requested-right string is displayed in the Details pane of the user authentication dialog box. Either this method or the [`setAuthorizationRights(_:)`](sfauthorizationview/setauthorizationrights(_:).md) method must be called before the view displays correctly.

## Parameters

- `authorizationString`: The string to be displayed.

## See Also

- [Authorization Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995)
- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](sfauthorizationview/authorizationrights.md)
  Returns the authorization rights for this view.
- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](sfauthorizationview/setauthorizationrights(_:).md)
  Sets the authorization rights for this view.
- [func setAutoupdate(Bool)](sfauthorizationview/setautoupdate(_:).md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](sfauthorizationview/setautoupdate(_:interval:).md)
  Sets the authorization view to update itself at a specific interval.
- [func setFlags(AuthorizationFlags)](sfauthorizationview/setflags(_:).md)
  Sets the current authorization flags for the view.
- [func setEnabled(Bool)](sfauthorizationview/setenabled(_:).md)
  Sets the current state of the authorization view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setstring(_:))*