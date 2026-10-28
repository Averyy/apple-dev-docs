# bezelStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text field’s bezel style, square or rounded.

**Availability**:
- macOS

## Declaration

```swift
var bezelStyle: NSTextField.BezelStyle { get set }
```

```objc
@property NSTextFieldBezelStyle bezelStyle;
```

## Discussion

To enable a bezel for a text field, set [`isBezeled`](./isbezeled.md) to [`true`](../../Swift/true.md), then set the bezel style. See [`NSTextField.BezelStyle`](./bezelstyle-swift.enum.md) for available bezel styles.

> **Note**:  When you set this property to [`NSTextField.BezelStyle.roundedBezel`](./bezelstyle-swift.enum/roundedbezel.md), the text field doesn’t wrap the text. It displays using a single line.

## See Also

### Controlling the background
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean value that controls whether the text field’s cell draws a background color behind the text.
- [var isBezeled: Bool](./isbezeled.md)
  A Boolean value that controls whether the text field draws a bezeled background around its contents.
- [NSTextField.BezelStyle](./bezelstyle-swift.enum.md)
  The style of bezel the text field displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/bezelstyle-swift.property)*