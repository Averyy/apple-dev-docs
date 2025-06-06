# lastKeyView()

**Framework**: Security Interface  
**Kind**: method

Returns the last view in the keyboard loop of the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func lastKeyView() -> NSView!
```

#### Discussion

The default return value of this method is `nil`. When the authorization plug-in calls this method, your subclass should return the last view in the keyboard loop of your custom [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) object.

## See Also

- [func firstKeyView() -> NSView!](sfauthorizationpluginview/firstkeyview.md)
  Returns the first view in the keyboard loop of the view.
- [func firstResponder() -> NSResponder!](sfauthorizationpluginview/firstresponder.md)
  Returns the view that should get focus for keyboard events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/lastkeyview())*