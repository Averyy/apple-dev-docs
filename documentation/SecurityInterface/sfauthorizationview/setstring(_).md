# setString(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the requested-right string to use with the default authorization rights set.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setString(_ authorizationString: AuthorizationString!)
```

```objc
- (void) setString:(AuthorizationString) authorizationString;
```

## Discussion

This is a convenience method that creates an authorization rights set when you specify only the name of the requested right. The requested-right string is displayed in the Details pane of the user authentication dialog box. Either this method or the [`setAuthorizationRights(_:)`](./setauthorizationrights%28_%29.md) method must be called before the view displays correctly.

## Parameters

- `authorizationString`: The string to be displayed.

## See Also

### Related Documentation
- [Authorization Services Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995)
- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](./authorizationrights%28%29.md)
  Returns the authorization rights for this view.
### Setting up the authorization view
- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](./setauthorizationrights%28_%29.md)
  Sets the authorization rights for this view.
- [func setAutoupdate(Bool)](./setautoupdate%28_%29.md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](./setautoupdate%28_,interval%29.md)
  Sets the authorization view to update itself at a specific interval.
- [func setFlags(AuthorizationFlags)](./setflags%28_%29.md)
  Sets the current authorization flags for the view.
- [func setEnabled(Bool)](./setenabled%28_%29.md)
  Sets the current state of the authorization view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setstring(_:))*