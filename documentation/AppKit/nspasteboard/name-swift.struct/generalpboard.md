# generalPboard

**Framework**: AppKit  
**Kind**: property

The pasteboard used for ordinary cut, copy, and paste operations.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let generalPboard: NSPasteboard.Name
```

#### Discussion

This pasteboard holds the contents of the last selection that’s been cut or copied.

## See Also

- [static let dragPboard: NSPasteboard.Name](nspasteboard/name-swift.struct/dragpboard.md)
  The pasteboard that stores data to be moved as the result of a drag operation.
- [static let findPboard: NSPasteboard.Name](nspasteboard/name-swift.struct/findpboard.md)
  The pasteboard that holds information about the current state of the active application’s find panel.
- [static let fontPboard: NSPasteboard.Name](nspasteboard/name-swift.struct/fontpboard.md)
  The pasteboard that holds font and character information and supports Copy Font and Paste Font commands that may be implemented in a text editor.
- [static let rulerPboard: NSPasteboard.Name](nspasteboard/name-swift.struct/rulerpboard.md)
  The pasteboard that holds information about paragraph formats and supports the Copy Ruler and Paste Ruler commands implemented in a text editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/name-swift.struct/generalpboard)*