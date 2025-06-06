# setButton(_:enabled:)

**Framework**: Security Interface  
**Kind**: method

Enables or disables a button in the authorization plug-in’s user interface.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setButton(_ inButtonType: SFButtonType, enabled inEnabled: Bool)
```

## Parameters

- `inButtonType`: The type of the button.
- `inEnabled`:   to enable the button,   to disable the button.

## See Also

- [func display()](sfauthorizationpluginview/display.md)
  Displays the user interface provided by the authorization plug-in view subclass.
- [func update()](sfauthorizationpluginview/update.md)
  Tells the authorization plug-in to get and display the appropriate view in the authorization plug-in’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/setbutton(_:enabled:))*