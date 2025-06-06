# textBackgroundColor

**Framework**: AppKit  
**Kind**: property

The color to use for the background area behind text.

**Availability**:
- macOS ?+

## Declaration

```swift
class var textBackgroundColor: NSColor { get }
```

#### Discussion

When text is selected, its background color changes to the return value of [`selectedTextBackgroundColor`](nscolor/selectedtextbackgroundcolor.md).

When applied to an [`NSBox`](nsbox.md) object, this color supports Desktop Tinting in Dark Mode. With Desktop Tinting, the system modifies this color dynamically by incorporating some of the color from the underlying desktop image. The system does not apply this dynamic tinting effect to other types of views.

## See Also

- [class var textColor: NSColor](nscolor/textcolor.md)
  The color to use for text.
- [class var placeholderTextColor: NSColor](nscolor/placeholdertextcolor.md)
  The color to use for placeholder text in controls or text views.
- [class var selectedTextColor: NSColor](nscolor/selectedtextcolor.md)
  The color to use for selected text.
- [class var selectedTextBackgroundColor: NSColor](nscolor/selectedtextbackgroundcolor.md)
  The color to use for the background of selected text.
- [class var keyboardFocusIndicatorColor: NSColor](nscolor/keyboardfocusindicatorcolor.md)
  The color to use for the keyboard focus ring around controls.
- [class var unemphasizedSelectedTextColor: NSColor](nscolor/unemphasizedselectedtextcolor.md)
  The color to use for selected text in an unemphasized context.
- [class var unemphasizedSelectedTextBackgroundColor: NSColor](nscolor/unemphasizedselectedtextbackgroundcolor.md)
  The color to use for the text background in an unemphasized context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/textbackgroundcolor)*