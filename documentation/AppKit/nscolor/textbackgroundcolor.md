# textBackgroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The color to use for the background area behind text.

**Availability**:
- macOS

## Declaration

```swift
class var textBackgroundColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * textBackgroundColor;
```

#### Discussion

When text is selected, its background color changes to the return value of [`selectedTextBackgroundColor`](./selectedtextbackgroundcolor.md).

When applied to an [`NSBox`](../nsbox.md) object, this color supports Desktop Tinting in Dark Mode. With Desktop Tinting, the system modifies this color dynamically by incorporating some of the color from the underlying desktop image. The system does not apply this dynamic tinting effect to other types of views.

## See Also

### Text colors
- [class var textColor: NSColor](./textcolor.md)
  The color to use for text.
- [class var placeholderTextColor: NSColor](./placeholdertextcolor.md)
  The color to use for placeholder text in controls or text views.
- [class var selectedTextColor: NSColor](./selectedtextcolor.md)
  The color to use for selected text.
- [class var selectedTextBackgroundColor: NSColor](./selectedtextbackgroundcolor.md)
  The color to use for the background of selected text.
- [class var keyboardFocusIndicatorColor: NSColor](./keyboardfocusindicatorcolor.md)
  The color to use for the keyboard focus ring around controls.
- [class var unemphasizedSelectedTextColor: NSColor](./unemphasizedselectedtextcolor.md)
  The color to use for selected text in an unemphasized context.
- [class var unemphasizedSelectedTextBackgroundColor: NSColor](./unemphasizedselectedtextbackgroundcolor.md)
  The color to use for the text background in an unemphasized context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/textbackgroundcolor)*