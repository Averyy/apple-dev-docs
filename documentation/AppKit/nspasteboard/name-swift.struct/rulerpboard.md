# rulerPboard

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The pasteboard that holds information about paragraph formats and supports the Copy Ruler and Paste Ruler commands implemented in a text editor.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13 (renamed: NSPasteboard.Name.ruler)

## Declaration

```swift
static let rulerPboard: NSPasteboard.Name
```

```c
extern NSPasteboardName NSRulerPboard;
```

## See Also

### Deprecated
- [static let dragPboard: NSPasteboard.Name](./dragpboard.md)
  The pasteboard that stores data to be moved as the result of a drag operation.
- [static let findPboard: NSPasteboard.Name](./findpboard.md)
  The pasteboard that holds information about the current state of the active application’s find panel.
- [static let fontPboard: NSPasteboard.Name](./fontpboard.md)
  The pasteboard that holds font and character information and supports Copy Font and Paste Font commands that may be implemented in a text editor.
- [static let generalPboard: NSPasteboard.Name](./generalpboard.md)
  The pasteboard used for ordinary cut, copy, and paste operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/name-swift.struct/rulerpboard)*