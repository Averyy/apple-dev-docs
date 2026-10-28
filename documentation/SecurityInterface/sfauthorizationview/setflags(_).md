# setFlags(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the current authorization flags for the view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setFlags(_ flags: AuthorizationFlags)
```

```objc
- (void) setFlags:(AuthorizationFlags) flags;
```

## Discussion

You can use this method to change the authorization flag settings made with the [`setAuthorizationRights(_:)`](./setauthorizationrights%28_%29.md) method or to specify flags other than the default ([`kAuthorizationFlagDefaults`](../../Security/authorizationflags/kauthorizationflagdefaults.md)) used by the [`setString(_:)`](./setstring%28_%29.md) method.

The authorization flags are described in Authorization Options in [Authorization Services](../../Security/authorization-services.md).

## Parameters

- `flags`: The authorization flags to set for this view.

## See Also

### Setting up the authorization view
- [func setString(AuthorizationString!)](./setstring%28_%29.md)
  Sets the requested-right string to use with the default authorization rights set.
- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](./setauthorizationrights%28_%29.md)
  Sets the authorization rights for this view.
- [func setAutoupdate(Bool)](./setautoupdate%28_%29.md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](./setautoupdate%28_,interval%29.md)
  Sets the authorization view to update itself at a specific interval.
- [func setEnabled(Bool)](./setenabled%28_%29.md)
  Sets the current state of the authorization view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview/setflags(_:))*