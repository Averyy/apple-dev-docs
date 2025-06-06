# firstKeyView()

**Framework**: Security Interface  
**Kind**: method

Returns the first view in the keyboard loop of the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func firstKeyView() -> NSView!
```

#### Discussion

The default return value of this method is `nil`. When the authorization plug-in calls this method, your subclass should return the first view in the keyboard loop of your custom [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) object.

## See Also

- [func firstResponder() -> NSResponder!](sfauthorizationpluginview/firstresponder.md)
  Returns the view that should get focus for keyboard events.
- [func lastKeyView() -> NSView!](sfauthorizationpluginview/lastkeyview.md)
  Returns the last view in the keyboard loop of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/firstkeyview())*