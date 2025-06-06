# init(labelWithString:)

**Framework**: AppKit  
**Kind**: init

Initializes a text field for use as a static label that uses the system default font, doesn’t wrap, and doesn’t have selectable text.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
convenience init(labelWithString stringValue: String)
```

#### Return Value

A text field that displays the specified string as a static label.

## Parameters

- `stringValue`: A string to use as the content of the label.

## See Also

- [convenience init(labelWithAttributedString: NSAttributedString)](nstextfield/init(labelwithattributedstring:).md)
  Creates a text field for use as a static label that displays styled text, doesn’t wrap, and doesn’t have selectable text.
- [convenience init(string: String)](nstextfield/init(string:).md)
  Initializes a single-line editable text field for user input using the system default font and standard visual appearance.
- [convenience init(wrappingLabelWithString: String)](nstextfield/init(wrappinglabelwithstring:).md)
  Initializes a text field for use as a multiline static label with selectable text that uses the system default font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/init(labelwithstring:))*