# NSPasteboard.Name

**Framework**: AppKit  
**Kind**: struct

Constants that represent the standard pasteboard names.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Name
```

## Topics

### Named Pasteboards
- [static let drag: NSPasteboard.Name](nspasteboard/name-swift.struct/drag.md)
  The pasteboard that stores data to move as the result of a drag operation.
- [static let find: NSPasteboard.Name](nspasteboard/name-swift.struct/find.md)
  The pasteboard that holds information about the current state of the active application’s find panel.
- [static let font: NSPasteboard.Name](nspasteboard/name-swift.struct/font.md)
  The pasteboard that holds font and character information and supports Copy Font and Paste Font commands that the text editor may implement.
- [static let general: NSPasteboard.Name](nspasteboard/name-swift.struct/general.md)
  The pasteboard you use to perform ordinary cut, copy, and paste operations.
- [static let ruler: NSPasteboard.Name](nspasteboard/name-swift.struct/ruler.md)
  The pasteboard that holds information about paragraph formats and supports the Copy Ruler and Paste Ruler commands that the text editor may implement.
### Deprecated
- [static let dragPboard: NSPasteboard.Name](nspasteboard/name-swift.struct/dragpboard.md)
  The pasteboard that stores data to be moved as the result of a drag operation.
- [static let findPboard: NSPasteboard.Name](nspasteboard/name-swift.struct/findpboard.md)
  The pasteboard that holds information about the current state of the active application’s find panel.
- [static let fontPboard: NSPasteboard.Name](nspasteboard/name-swift.struct/fontpboard.md)
  The pasteboard that holds font and character information and supports Copy Font and Paste Font commands that may be implemented in a text editor.
- [static let generalPboard: NSPasteboard.Name](nspasteboard/name-swift.struct/generalpboard.md)
  The pasteboard used for ordinary cut, copy, and paste operations.
- [static let rulerPboard: NSPasteboard.Name](nspasteboard/name-swift.struct/rulerpboard.md)
  The pasteboard that holds information about paragraph formats and supports the Copy Ruler and Paste Ruler commands implemented in a text editor.
### Initializers
- [init(String)](nspasteboard/name-swift.struct/init(_:).md)
- [init(rawValue: String)](nspasteboard/name-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class var general: NSPasteboard](nspasteboard/general.md)
  The shared pasteboard object to use for general content.
- [init(byFilteringData: Data, ofType: NSPasteboard.PasteboardType)](nspasteboard/init(byfilteringdata:oftype:).md)
  Creates a new pasteboard object that supplies the specified data in as many types as possible based on the available filter services.
- [init(byFilteringFile: String)](nspasteboard/init(byfilteringfile:).md)
  Creates a new pasteboard object that supplies the specified file in as many types as possible based on the available filter services.
- [init(byFilteringTypesInPasteboard: NSPasteboard)](nspasteboard/init(byfilteringtypesinpasteboard:).md)
  Creates a new pasteboard object that supplies the specified pasteboard data in as many types as possible based on the available filter services.
- [init(name: NSPasteboard.Name)](nspasteboard/init(name:).md)
  Returns the pasteboard with the specified name.
- [class func withUniqueName() -> NSPasteboard](nspasteboard/withuniquename.md)
  Creates and returns a new pasteboard with a name that is guaranteed to be unique with respect to other pasteboards in the system.
- [func releaseGlobally()](nspasteboard/releaseglobally.md)
  Releases the receiver’s resources in the pasteboard server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/name-swift.struct)*