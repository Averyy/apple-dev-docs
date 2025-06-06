# init(wrappingLabelWithString:)

**Framework**: AppKit  
**Kind**: init

Initializes a text field for use as a multiline static label with selectable text that uses the system default font.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
convenience init(wrappingLabelWithString stringValue: String)
```

#### Return Value

A multiline text field that displays the specified string.

## Parameters

- `stringValue`: A string to use as the initial content of the editable text field.

## See Also

- [convenience init(labelWithAttributedString: NSAttributedString)](nstextfield/init(labelwithattributedstring:).md)
  Creates a text field for use as a static label that displays styled text, doesn’t wrap, and doesn’t have selectable text.
- [convenience init(labelWithString: String)](nstextfield/init(labelwithstring:).md)
  Initializes a text field for use as a static label that uses the system default font, doesn’t wrap, and doesn’t have selectable text.
- [convenience init(string: String)](nstextfield/init(string:).md)
  Initializes a single-line editable text field for user input using the system default font and standard visual appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/init(wrappinglabelwithstring:))*