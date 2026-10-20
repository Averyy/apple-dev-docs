# setButton(_:enabled:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Enables or disables a button in the authorization plug-in’s user interface.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setButton(_ inButtonType: SFButtonType, enabled inEnabled: Bool)
```

```objc
- (void) setButton:(SFButtonType) inButtonType enabled:(BOOL) inEnabled;
```

## Parameters

- `inButtonType`: The type of the button.
- `inEnabled`: [`true`](../../Swift/true.md) to enable the button, [`false`](../../Swift/false.md) to disable the button.

## See Also

### Communicating with the Authorization Plug-in
- [func display()](./display%28%29.md)
  Displays the user interface provided by the authorization plug-in view subclass.
- [func update()](./update%28%29.md)
  Tells the authorization plug-in to get and display the appropriate view in the authorization plug-in’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/setbutton(_:enabled:))*