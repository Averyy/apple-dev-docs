# font

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The pasteboard that holds font and character information and supports Copy Font and Paste Font commands that the text editor may implement.

**Availability**:
- macOS 10.13+

## Declaration

```swift
static let font: NSPasteboard.Name
```

```c
extern NSPasteboardName NSPasteboardNameFont;
```

## See Also

### Named Pasteboards
- [static let drag: NSPasteboard.Name](./drag.md)
  The pasteboard that stores data to move as the result of a drag operation.
- [static let find: NSPasteboard.Name](./find.md)
  The pasteboard that holds information about the current state of the active application’s find panel.
- [static let general: NSPasteboard.Name](./general.md)
  The pasteboard you use to perform ordinary cut, copy, and paste operations.
- [static let ruler: NSPasteboard.Name](./ruler.md)
  The pasteboard that holds information about paragraph formats and supports the Copy Ruler and Paste Ruler commands that the text editor may implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/name-swift.struct/font)*