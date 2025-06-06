# drawsBackground

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the text field’s cell draws a background color behind the text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var drawsBackground: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the text field’s cell draws a background; if [`false`](https://developer.apple.com/documentation/swift/false), it draws nothing behind the text.

To prevent inconsistent rendering, `NSTextField` disables background color rendering for text fields with rounded bezels.

## See Also

- [var backgroundColor: NSColor?](nstextfield/backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var isBezeled: Bool](nstextfield/isbezeled.md)
  A Boolean value that controls whether the text field draws a bezeled background around its contents.
- [var bezelStyle: NSTextField.BezelStyle](nstextfield/bezelstyle-swift.property.md)
  The text field’s bezel style, square or rounded.
- [NSTextField.BezelStyle](nstextfield/bezelstyle-swift.enum.md)
  The style of bezel the text field displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/drawsbackground)*