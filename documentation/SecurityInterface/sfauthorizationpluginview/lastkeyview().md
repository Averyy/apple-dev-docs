# lastKeyView()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the last view in the keyboard loop of the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func lastKeyView() -> NSView!
```

```objc
- (NSView *) lastKeyView;
```

#### Discussion

The default return value of this method is `nil`. When the authorization plug-in calls this method, your subclass should return the last view in the keyboard loop of your custom [`NSView`](../../AppKit/nsview.md) object.

## See Also

### Setting Up the Keyboard Loop
- [func firstKeyView() -> NSView!](./firstkeyview%28%29.md)
  Returns the first view in the keyboard loop of the view.
- [func firstResponder() -> NSResponder!](./firstresponder%28%29.md)
  Returns the view that should get focus for keyboard events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/lastkeyview())*