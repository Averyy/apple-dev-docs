# didActivate()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Tells the authorization plug-in when its user interface has become active.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func didActivate()
```

```objc
- (void) didActivate;
```

## See Also

### Configuring the User Interface
- [func didDeactivate()](./diddeactivate%28%29.md)
  Tells the authorization plug-in that its user interface has been deactivated.
- [func willActivate(withUser: [AnyHashable : Any]!)](./willactivate%28withuser%29.md)
  Tells the authorization plug-in that its user interface is about to be made active by the Apple-provided Security Agent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/didactivate())*