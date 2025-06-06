# setTarget(_:)

**Framework**: AppKit  
**Kind**: method

Sets the target of the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setTarget(_ target: Any?)
```

## Parameters

- `target`: The target of the receiver. When you select a color in the color panel   sends its action to its target, provided that neither the action nor the target is  . The target is   by default.

## See Also

- [class NSColorPanel](nscolorpanel.md)
  A standard user interface for selecting color in an app.
- [var accessoryView: NSView?](nscolorpanel/accessoryview.md)
  The accessory view.
- [var isContinuous: Bool](nscolorpanel/iscontinuous.md)
  A Boolean value indicating whether the receiver continuously sends the action message to the target.
- [func setAction(Selector?)](nscolorpanel/setaction(_:).md)
  Sets the color panel’s action message.
- [var showsAlpha: Bool](nscolorpanel/showsalpha.md)
  A Boolean value that indicates whether the receiver shows alpha values and an opacity slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/settarget(_:))*