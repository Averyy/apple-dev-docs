# deleteWordBackward(_:)

**Framework**: AppKit  
**Kind**: method

Deletes the word preceding the current insertion point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func deleteWordBackward(_ sender: Any?)
```

#### Discussion

If the insertion point is in the middle of a word, this method deletes only the portion of the word preceding the insertion point.

## See Also

- [func deleteBackward(Any?)](nsstandardkeybindingresponding/deletebackward(_:).md)
  Deletes content moving backward from the current insertion point.
- [func deleteBackwardByDecomposingPreviousCharacter(Any?)](nsstandardkeybindingresponding/deletebackwardbydecomposingpreviouscharacter(_:).md)
- [func deleteForward(Any?)](nsstandardkeybindingresponding/deleteforward(_:).md)
- [func deleteToBeginningOfLine(Any?)](nsstandardkeybindingresponding/deletetobeginningofline(_:).md)
  Deletes content from the insertion point to the beginning of the current line.
- [func deleteToBeginningOfParagraph(Any?)](nsstandardkeybindingresponding/deletetobeginningofparagraph(_:).md)
  Deletes content from the insertion point to the beginning of the current paragraph.
- [func deleteToEndOfLine(Any?)](nsstandardkeybindingresponding/deletetoendofline(_:).md)
  Deletes content from the insertion point to the end of the current line.
- [func deleteToEndOfParagraph(Any?)](nsstandardkeybindingresponding/deletetoendofparagraph(_:).md)
  Deletes content from the insertion point to the end of the current paragraph.
- [func deleteWordForward(Any?)](nsstandardkeybindingresponding/deletewordforward(_:).md)
- [func yank(Any?)](nsstandardkeybindingresponding/yank(_:).md)
  Deletes the current selection, placing it in a temporary buffer, such as the Clipboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstandardkeybindingresponding/deletewordbackward(_:))*