# init(wrappingLabelWithString:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a text field for use as a multiline static label with selectable text that uses the system default font.

**Availability**:
- macOS 10.12+

## Declaration

```swift
convenience init(wrappingLabelWithString stringValue: String)
```

```objc
+ (instancetype) wrappingLabelWithString:(NSString *) stringValue;
```

## Return Value

A multiline text field that displays the specified string.

## Parameters

- `stringValue`: A string to use as the initial content of the editable text field.

## See Also

### Creating text fields
- [convenience init(labelWithAttributedString: NSAttributedString)](./init%28labelwithattributedstring%29.md)
  Creates a text field for use as a static label that displays styled text, doesn’t wrap, and doesn’t have selectable text.
- [convenience init(labelWithString: String)](./init%28labelwithstring%29.md)
  Initializes a text field for use as a static label that uses the system default font, doesn’t wrap, and doesn’t have selectable text.
- [convenience init(string: String)](./init%28string%29.md)
  Initializes a single-line editable text field for user input using the system default font and standard visual appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/init(wrappinglabelwithstring:))*