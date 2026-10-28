# insertText(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts `aString` into the receiver’s text at the insertion point if there is one, otherwise replacing the selection.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use `NSTextInputClient` method [`insertText(_:replacementRange:)`](../nstextinputclient/inserttext%28_,replacementrange%29.md) instead.

## Declaration

```swift
func insertText(_ insertString: Any)
```

```objc
- (void) insertText:(id) insertString;
```

## Discussion

The inserted text is assigned the current typing attributes.

This method is the means by which text typed by the user enters an NSTextView. See the [`NSInputManager`](../nsinputmanager.md) class and [`NSTextInput`](../nstextinput.md) protocol specifications for more information.

This method is the entry point for inserting text typed by the user and is generally not suitable for other purposes. Programmatic modification of the text is best done by operating on the text storage directly. Because this method pertains to the actions of the user, the text view must be editable for the insertion to work.

## Parameters

- `insertString`: The string to insert. `aString` can be either an [`NSString`](../../Foundation/nsstring.md) object or an [`NSAttributedString`](../../Foundation/nsattributedstring.md) object.

## See Also

### Related Documentation
- [var typingAttributes: [NSAttributedString.Key : Any]](./typingattributes.md)
  The receiver’s typing attributes.
### Deprecated
- [func toggleTraditionalCharacterShape(Any?)](./toggletraditionalcharactershape%28_%29.md)
  Toggles the `NSCharacterShapeAttributeName` attribute at the current selection.
- [- toggleBaseWritingDirection:](./togglebasewritingdirection_.md)
  Changes the base writing direction of a paragraph between left-to-right and right-to-left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/inserttext(_:))*