# buttonPressed(_:)

**Framework**: Security Interface  
**Kind**: method

Tells the authorization plug-in that the user pressed a button in the custom view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func buttonPressed(_ inButtonType: SFButtonType)
```

#### Discussion

By default, [`buttonPressed(_:)`](sfauthorizationpluginview/buttonpressed(_:).md) will set a result of Deny when the OK or Login buttons are pressed. An [`SFAuthorizationPluginView`](sfauthorizationpluginview.md) subclass needs to override this method to set the context values for the short name of the user so that user attributes can be looked up. To do this, use [`kAuthorizationEnvironmentUsername`](https://developer.apple.com/documentation/Security/kAuthorizationEnvironmentUsername) as the key. A subclass should also set any additional context values that are needed by the authorization plug-in to verify the user’s credentials. To do this, use the appropriate function pointers you receive from [`callbacks()`](sfauthorizationpluginview/callbacks().md).

When you override this method, do not call `[super buttonPressed]`.

## Parameters

- `inButtonType`: The type of button that was pressed.

## See Also

- [func view(for: SFViewType) -> NSView!](sfauthorizationpluginview/view(for:).md)
  Returns the appropriate view object for the specified view type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/buttonpressed(_:))*