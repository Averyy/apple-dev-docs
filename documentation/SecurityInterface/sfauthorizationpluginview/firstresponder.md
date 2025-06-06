# firstResponder()

**Framework**: Security Interface  
**Kind**: method

Returns the view that should get focus for keyboard events.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func firstResponder() -> NSResponder!
```

#### Discussion

The default return value of this method is `nil`. When the authorization plug-in calls this method, your subclass should return the view that should get the focus for keyboard events.

## See Also

- [func firstKeyView() -> NSView!](sfauthorizationpluginview/firstkeyview.md)
  Returns the first view in the keyboard loop of the view.
- [func lastKeyView() -> NSView!](sfauthorizationpluginview/lastkeyview.md)
  Returns the last view in the keyboard loop of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/firstresponder())*