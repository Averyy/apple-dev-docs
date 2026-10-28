# drawsBackground

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the text field’s cell draws a background color behind the text.

**Availability**:
- macOS

## Declaration

```swift
var drawsBackground: Bool { get set }
```

```objc
@property BOOL drawsBackground;
```

## Discussion

If [`true`](../../Swift/true.md), the text field’s cell draws a background; if [`false`](../../Swift/false.md), it draws nothing behind the text.

To prevent inconsistent rendering, `NSTextField` disables background color rendering for text fields with rounded bezels.

## See Also

### Controlling the background
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var isBezeled: Bool](./isbezeled.md)
  A Boolean value that controls whether the text field draws a bezeled background around its contents.
- [var bezelStyle: NSTextField.BezelStyle](./bezelstyle-swift.property.md)
  The text field’s bezel style, square or rounded.
- [NSTextField.BezelStyle](./bezelstyle-swift.enum.md)
  The style of bezel the text field displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/drawsbackground)*