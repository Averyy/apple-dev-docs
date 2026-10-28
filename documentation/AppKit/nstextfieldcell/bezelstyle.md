# bezelStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The bezel style to use when drawing the text field.

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

To set the bezel style, you must have already set the the text field’s [`isBezeled`](../nstextfield/isbezeled.md) method with an argument of [`true`](../../Swift/true.md). For a list of bezel styles, see [`NSTextField.BezelStyle`](../nstextfield/bezelstyle-swift.enum.md).

## See Also

### Setting the Bezel Style
- [NSTextField.BezelStyle](../nstextfield/bezelstyle-swift.enum.md)
  The style of bezel the text field displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/bezelstyle)*