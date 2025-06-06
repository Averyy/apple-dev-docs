# bezelStyle

**Framework**: AppKit  
**Kind**: property

The bezel style to use when drawing the text field.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var bezelStyle: NSTextField.BezelStyle { get set }
```

#### Discussion

To set the bezel style, you must have already set the the text field’s [`isBezeled`](nstextfield/isbezeled.md) method with an argument of [`true`](https://developer.apple.com/documentation/swift/true). For a list of bezel styles, see [`NSTextField.BezelStyle`](nstextfield/bezelstyle-swift.enum.md).

## See Also

- [NSTextField.BezelStyle](nstextfield/bezelstyle-swift.enum.md)
  The style of bezel the text field displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/bezelstyle)*