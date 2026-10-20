# firstResponder()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the view that should get focus for keyboard events.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func firstResponder() -> NSResponder!
```

```objc
- (NSResponder *) firstResponder;
```

#### Discussion

The default return value of this method is `nil`. When the authorization plug-in calls this method, your subclass should return the view that should get the focus for keyboard events.

## See Also

### Setting Up the Keyboard Loop
- [func firstKeyView() -> NSView!](./firstkeyview%28%29.md)
  Returns the first view in the keyboard loop of the view.
- [func lastKeyView() -> NSView!](./lastkeyview%28%29.md)
  Returns the last view in the keyboard loop of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/firstresponder())*