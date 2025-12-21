# isBezeled

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the text field draws a bezeled background around its contents.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isBezeled: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the text field draws a bezel and sets [`drawsBackground`](nstextfield/drawsbackground.md) to [`false`](https://developer.apple.com/documentation/Swift/false); if [`false`](https://developer.apple.com/documentation/Swift/false), it doesn’t draw a bezeled background.

## See Also

- [var backgroundColor: NSColor?](nstextfield/backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var drawsBackground: Bool](nstextfield/drawsbackground.md)
  A Boolean value that controls whether the text field’s cell draws a background color behind the text.
- [var bezelStyle: NSTextField.BezelStyle](nstextfield/bezelstyle-swift.property.md)
  The text field’s bezel style, square or rounded.
- [NSTextField.BezelStyle](nstextfield/bezelstyle-swift.enum.md)
  The style of bezel the text field displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/isbezeled)*