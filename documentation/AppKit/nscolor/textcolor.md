# textColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The color to use for text.

**Availability**:
- macOS

## Declaration

```swift
class var textColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * textColor;
```

## Discussion

When text is selected, its color changes to the return value of [`selectedTextColor`](./selectedtextcolor.md).

## See Also

### Text colors
- [class var placeholderTextColor: NSColor](./placeholdertextcolor.md)
  The color to use for placeholder text in controls or text views.
- [class var selectedTextColor: NSColor](./selectedtextcolor.md)
  The color to use for selected text.
- [class var textBackgroundColor: NSColor](./textbackgroundcolor.md)
  The color to use for the background area behind text.
- [class var selectedTextBackgroundColor: NSColor](./selectedtextbackgroundcolor.md)
  The color to use for the background of selected text.
- [class var keyboardFocusIndicatorColor: NSColor](./keyboardfocusindicatorcolor.md)
  The color to use for the keyboard focus ring around controls.
- [class var unemphasizedSelectedTextColor: NSColor](./unemphasizedselectedtextcolor.md)
  The color to use for selected text in an unemphasized context.
- [class var unemphasizedSelectedTextBackgroundColor: NSColor](./unemphasizedselectedtextbackgroundcolor.md)
  The color to use for the text background in an unemphasized context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/textcolor)*