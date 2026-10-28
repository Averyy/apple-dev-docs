# firstKeyView()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the first view in the keyboard loop of the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func firstKeyView() -> NSView!
```

```objc
- (NSView *) firstKeyView;
```

## Discussion

The default return value of this method is `nil`. When the authorization plug-in calls this method, your subclass should return the first view in the keyboard loop of your custom [`NSView`](../../AppKit/nsview.md) object.

## See Also

### Setting Up the Keyboard Loop
- [func firstResponder() -> NSResponder!](./firstresponder%28%29.md)
  Returns the view that should get focus for keyboard events.
- [func lastKeyView() -> NSView!](./lastkeyview%28%29.md)
  Returns the last view in the keyboard loop of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/firstkeyview())*