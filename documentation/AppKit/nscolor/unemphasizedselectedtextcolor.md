# unemphasizedSelectedTextColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The color to use for selected text in an unemphasized context.

**Availability**:
- macOS 10.14+

## Declaration

```swift
class var unemphasizedSelectedTextColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * unemphasizedSelectedTextColor;
```

## Discussion

Use this color when the window containing the text is not key, or when the view containing the text does not have key focus.

## See Also

### Text colors
- [class var textColor: NSColor](./textcolor.md)
  The color to use for text.
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
- [class var unemphasizedSelectedTextBackgroundColor: NSColor](./unemphasizedselectedtextbackgroundcolor.md)
  The color to use for the text background in an unemphasized context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedtextcolor)*