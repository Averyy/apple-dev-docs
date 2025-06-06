# allowsEditingTextAttributes

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether the user can change font attributes of the text field’s string.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsEditingTextAttributes: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), and the text value is an attributed string, the text field’s content displays using the attributed string’s visual settings. The user can modify the text field’s style attributes in the font panel.

If [`false`](https://developer.apple.com/documentation/swift/false), and the text is an attributed string, the text field ignores style attributes, such as font and color. The text field’s content displays according to the text field’s settings. The text field ignores changes to the attributed string’s attributes when displaying the string and when the text field is in edit mode.

## See Also

- [var importsGraphics: Bool](nstextfield/importsgraphics.md)
  A Boolean value that controls whether the user can drag image files into the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/allowseditingtextattributes)*