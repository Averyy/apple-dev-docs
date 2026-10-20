# setAction(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the color panel’s action message.

**Availability**:
- macOS

## Declaration

```swift
func setAction(_ selector: Selector?)
```

```objc
- (void) setAction:(SEL) selector;
```

#### Discussion

When you select a color in the color panel `NSColorPanel` sends its action to its target, provided that neither the action nor the target is `nil`. The action is `NULL` by default.

## Parameters

- `selector`: The action message.

## See Also

### Configuring the color panel
- [var accessoryView: NSView?](./accessoryview.md)
  The accessory view.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value indicating whether the receiver continuously sends the action message to the target.
- [func setTarget(Any?)](./settarget%28_%29.md)
  Sets the target of the receiver.
- [var showsAlpha: Bool](./showsalpha.md)
  A Boolean value that indicates whether the receiver shows alpha values and an opacity slider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/setaction(_:))*