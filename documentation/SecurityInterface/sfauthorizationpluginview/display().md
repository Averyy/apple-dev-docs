# display()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Displays the user interface provided by the authorization plug-in view subclass.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func display()
```

```objc
- (void) displayView;
```

## Discussion

It’s not likely that you will want to override this method, but if you do, be sure to call `[super displayView]`. If you don’t call `[super displayView]`, your custom view will not get displayed.

This method will raise an [`SFDisplayViewException`](../sfdisplayviewexception.md) exception if an error occurs while displaying the authorization dialog.

## See Also

### Communicating with the Authorization Plug-in
- [func setButton(SFButtonType, enabled: Bool)](./setbutton%28_,enabled%29.md)
  Enables or disables a button in the authorization plug-in’s user interface.
- [func update()](./update%28%29.md)
  Tells the authorization plug-in to get and display the appropriate view in the authorization plug-in’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/display())*