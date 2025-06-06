# willActivate(withUser:)

**Framework**: Security Interface  
**Kind**: method

Tells the authorization plug-in that its user interface is about to be made active by the Apple-provided Security Agent.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func willActivate(withUser inUserInformation: [AnyHashable : Any]!)
```

#### Discussion

Your [`SFAuthorizationPluginView`](sfauthorizationpluginview.md) instance can use the user name to pre-populate a text field in the user interface.

## Parameters

- `inUserInformation`: Note:   may be  .

## See Also

- [func didActivate()](sfauthorizationpluginview/didactivate.md)
  Tells the authorization plug-in when its user interface has become active.
- [func didDeactivate()](sfauthorizationpluginview/diddeactivate.md)
  Tells the authorization plug-in that its user interface has been deactivated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/willactivate(withuser:))*