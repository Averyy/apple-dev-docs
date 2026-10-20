# setTarget(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the target of the receiver.

**Availability**:
- macOS

## Declaration

```swift
func setTarget(_ target: Any?)
```

```objc
- (void) setTarget:(id) target;
```

## Parameters

- `target`: The target of the receiver. When you select a color in the color panel `NSColorPanel` sends its action to its target, provided that neither the action nor the target is `nil`. The target is `nil` by default.

## See Also

### Related Documentation
- [class NSColorPanel](../nscolorpanel.md)
  A standard user interface for selecting color in an app.
### Configuring the color panel
- [var accessoryView: NSView?](./accessoryview.md)
  The accessory view.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value indicating whether the receiver continuously sends the action message to the target.
- [func setAction(Selector?)](./setaction%28_%29.md)
  Sets the color panel’s action message.
- [var showsAlpha: Bool](./showsalpha.md)
  A Boolean value that indicates whether the receiver shows alpha values and an opacity slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/settarget(_:))*