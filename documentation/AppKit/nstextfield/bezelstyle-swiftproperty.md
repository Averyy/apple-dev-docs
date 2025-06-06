# bezelStyle

**Framework**: Appkit  
**Kind**: property

The text field’s bezel style, square or rounded.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var bezelStyle: NSTextField.BezelStyle { get set }
```

#### Discussion

To enable a bezel for a text field, set [`isBezeled`](nstextfield/isbezeled.md) to [`true`](https://developer.apple.com/documentation/swift/true), then set the bezel style. See [`NSTextField.BezelStyle`](nstextfield/bezelstyle-swift.enum.md) for available bezel styles.

> **Note**:  When you set this property to [`NSTextField.BezelStyle.roundedBezel`](nstextfield/bezelstyle-swift.enum/roundedbezel.md), the text field doesn’t wrap the text. It displays using a single line.

## See Also

- [var backgroundColor: NSColor?](nstextfield/backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var drawsBackground: Bool](nstextfield/drawsbackground.md)
  A Boolean value that controls whether the text field’s cell draws a background color behind the text.
- [var isBezeled: Bool](nstextfield/isbezeled.md)
  A Boolean value that controls whether the text field draws a bezeled background around its contents.
- [NSTextField.BezelStyle](nstextfield/bezelstyle-swift.enum.md)
  The style of bezel the text field displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/bezelstyle-swift.property)*