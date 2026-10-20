# NSPasteboard.Name

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that represent the standard pasteboard names.

**Availability**:
- macOS

## Declaration

```swift
struct Name
```

```c
typedef NSString * NSPasteboardName;
```

## Topics

### Named Pasteboards
- [static let drag: NSPasteboard.Name](./name-swift.struct/drag.md)
  The pasteboard that stores data to move as the result of a drag operation.
- [static let find: NSPasteboard.Name](./name-swift.struct/find.md)
  The pasteboard that holds information about the current state of the active application’s find panel.
- [static let font: NSPasteboard.Name](./name-swift.struct/font.md)
  The pasteboard that holds font and character information and supports Copy Font and Paste Font commands that the text editor may implement.
- [static let general: NSPasteboard.Name](./name-swift.struct/general.md)
  The pasteboard you use to perform ordinary cut, copy, and paste operations.
- [static let ruler: NSPasteboard.Name](./name-swift.struct/ruler.md)
  The pasteboard that holds information about paragraph formats and supports the Copy Ruler and Paste Ruler commands that the text editor may implement.
### Initializers
- [init(String)](./name-swift.struct/init%28_%29.md)
- [init(rawValue: String)](./name-swift.struct/init%28rawvalue%29.md)
### Deprecated
- [static let dragPboard: NSPasteboard.Name](./name-swift.struct/dragpboard.md)
  The pasteboard that stores data to be moved as the result of a drag operation.
- [static let findPboard: NSPasteboard.Name](./name-swift.struct/findpboard.md)
  The pasteboard that holds information about the current state of the active application’s find panel.
- [static let fontPboard: NSPasteboard.Name](./name-swift.struct/fontpboard.md)
  The pasteboard that holds font and character information and supports Copy Font and Paste Font commands that may be implemented in a text editor.
- [static let generalPboard: NSPasteboard.Name](./name-swift.struct/generalpboard.md)
  The pasteboard used for ordinary cut, copy, and paste operations.
- [static let rulerPboard: NSPasteboard.Name](./name-swift.struct/rulerpboard.md)
  The pasteboard that holds information about paragraph formats and supports the Copy Ruler and Paste Ruler commands implemented in a text editor.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating and releasing a pasteboard
- [class var general: NSPasteboard](./general.md)
  The shared pasteboard object to use for general content.
- [init(byFilteringData: Data, ofType: NSPasteboard.PasteboardType)](./init%28byfilteringdata,oftype%29.md)
  Creates a new pasteboard object that supplies the specified data in as many types as possible based on the available filter services.
- [init(byFilteringFile: String)](./init%28byfilteringfile%29.md)
  Creates a new pasteboard object that supplies the specified file in as many types as possible based on the available filter services.
- [init(byFilteringTypesInPasteboard: NSPasteboard)](./init%28byfilteringtypesinpasteboard%29.md)
  Creates a new pasteboard object that supplies the specified pasteboard data in as many types as possible based on the available filter services.
- [init(name: NSPasteboard.Name)](./init%28name%29.md)
  Returns the pasteboard with the specified name.
- [class func withUniqueName() -> NSPasteboard](./withuniquename%28%29.md)
  Creates and returns a new pasteboard with a name that is guaranteed to be unique with respect to other pasteboards in the system.
- [func releaseGlobally()](./releaseglobally%28%29.md)
  Releases the receiver’s resources in the pasteboard server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/name-swift.struct)*