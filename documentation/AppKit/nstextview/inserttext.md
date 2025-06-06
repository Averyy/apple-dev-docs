# insertText(_:)

**Framework**: AppKit  
**Kind**: method

Inserts `aString` into the receiver’s text at the insertion point if there is one, otherwise replacing the selection.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func insertText(_ insertString: Any)
```

#### Discussion

The inserted text is assigned the current typing attributes.

This method is the means by which text typed by the user enters an NSTextView. See the [`NSInputManager`](nsinputmanager.md) class and [`NSTextInput`](nstextinput.md) protocol specifications for more information.

This method is the entry point for inserting text typed by the user and is generally not suitable for other purposes. Programmatic modification of the text is best done by operating on the text storage directly. Because this method pertains to the actions of the user, the text view must be editable for the insertion to work.

## Parameters

- `insertString`: The string to insert.   can be either an   object or an   object.

## See Also

- [var typingAttributes: [NSAttributedString.Key : Any]](nstextview/typingattributes.md)
  The receiver’s typing attributes.
- [var allowedInputSourceLocales: [String]?](nstextview/allowedinputsourcelocales.md)
  An array of locale identifiers representing input sources that are allowed to be enabled when the receiver has the keyboard focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/inserttext(_:))*