# isBezeled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the text field draws a bezeled background around its contents.

**Availability**:
- macOS

## Declaration

```swift
var isBezeled: Bool { get set }
```

```objc
@property (getter=isBezeled) BOOL bezeled;
```

#### Discussion

If [`true`](../../Swift/true.md), the text field draws a bezel and sets [`drawsBackground`](./drawsbackground.md) to [`false`](../../Swift/false.md); if [`false`](../../Swift/false.md), it doesn’t draw a bezeled background.

## See Also

### Controlling the background
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean value that controls whether the text field’s cell draws a background color behind the text.
- [var bezelStyle: NSTextField.BezelStyle](./bezelstyle-swift.property.md)
  The text field’s bezel style, square or rounded.
- [NSTextField.BezelStyle](./bezelstyle-swift.enum.md)
  The style of bezel the text field displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/isbezeled)*