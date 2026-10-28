# allowsEditingTextAttributes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the user can change font attributes of the text field’s string.

**Availability**:
- macOS

## Declaration

```swift
var allowsEditingTextAttributes: Bool { get set }
```

```objc
@property BOOL allowsEditingTextAttributes;
```

## Discussion

If [`true`](../../Swift/true.md), and the text value is an attributed string, the text field’s content displays using the attributed string’s visual settings. The user can modify the text field’s style attributes in the font panel.

If [`false`](../../Swift/false.md), and the text is an attributed string, the text field ignores style attributes, such as font and color. The text field’s content displays according to the text field’s settings. The text field ignores changes to the attributed string’s attributes when displaying the string and when the text field is in edit mode.

## See Also

### Controlling rich text behavior
- [var importsGraphics: Bool](./importsgraphics.md)
  A Boolean value that controls whether the user can drag image files into the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/allowseditingtextattributes)*