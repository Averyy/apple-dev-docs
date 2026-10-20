# findPboard

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The pasteboard that holds information about the current state of the active application’s find panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13 (renamed: NSPasteboard.Name.find)

## Declaration

```swift
static let findPboard: NSPasteboard.Name
```

```c
extern NSPasteboardName NSFindPboard;
```

#### Discussion

This information permits users to enter a search string into the find panel, then switch to another application to conduct another search.

## See Also

### Deprecated
- [static let dragPboard: NSPasteboard.Name](./dragpboard.md)
  The pasteboard that stores data to be moved as the result of a drag operation.
- [static let fontPboard: NSPasteboard.Name](./fontpboard.md)
  The pasteboard that holds font and character information and supports Copy Font and Paste Font commands that may be implemented in a text editor.
- [static let generalPboard: NSPasteboard.Name](./generalpboard.md)
  The pasteboard used for ordinary cut, copy, and paste operations.
- [static let rulerPboard: NSPasteboard.Name](./rulerpboard.md)
  The pasteboard that holds information about paragraph formats and supports the Copy Ruler and Paste Ruler commands implemented in a text editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/name-swift.struct/findpboard)*