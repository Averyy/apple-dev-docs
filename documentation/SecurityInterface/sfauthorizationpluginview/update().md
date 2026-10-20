# update()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Tells the authorization plug-in to get and display the appropriate view in the authorization plug-in’s user interface.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func update()
```

```objc
- (void) updateView;
```

#### Discussion

Your subclass of [`SFAuthorizationPluginView`](../sfauthorizationpluginview.md) should call this method when a user clicks a button in your view that should result in a new view being displayed. Calling this method causes the authorization plug-in to get the new view and display it.

## See Also

### Communicating with the Authorization Plug-in
- [func display()](./display%28%29.md)
  Displays the user interface provided by the authorization plug-in view subclass.
- [func setButton(SFButtonType, enabled: Bool)](./setbutton%28_,enabled%29.md)
  Enables or disables a button in the authorization plug-in’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/update())*