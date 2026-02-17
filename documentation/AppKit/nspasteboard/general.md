# general

**Framework**: AppKit  
**Kind**: property

The shared pasteboard object to use for general content.

**Availability**:
- macOS ?+

## Declaration

```swift
class var general: NSPasteboard { get }
```

#### Return Value

The general pasteboard.

#### Discussion

Invokes [`init(name:)`](nspasteboard/init(name:).md) to obtain the pasteboard.

## See Also

- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [class NSPasteboard](nspasteboard.md)
  An object that transfers data to and from the pasteboard server.
- [Services Functions](services-functions.md)
  Configure the contents of your app’s Services menu.
- [init(byFilteringData: Data, ofType: NSPasteboard.PasteboardType)](nspasteboard/init(byfilteringdata:oftype:).md)
  Creates a new pasteboard object that supplies the specified data in as many types as possible based on the available filter services.
- [init(byFilteringFile: String)](nspasteboard/init(byfilteringfile:).md)
  Creates a new pasteboard object that supplies the specified file in as many types as possible based on the available filter services.
- [init(byFilteringTypesInPasteboard: NSPasteboard)](nspasteboard/init(byfilteringtypesinpasteboard:).md)
  Creates a new pasteboard object that supplies the specified pasteboard data in as many types as possible based on the available filter services.
- [init(name: NSPasteboard.Name)](nspasteboard/init(name:).md)
  Returns the pasteboard with the specified name.
- [NSPasteboard.Name](nspasteboard/name-swift.struct.md)
  Constants that represent the standard pasteboard names.
- [class func withUniqueName() -> NSPasteboard](nspasteboard/withuniquename.md)
  Creates and returns a new pasteboard with a name that is guaranteed to be unique with respect to other pasteboards in the system.
- [func releaseGlobally()](nspasteboard/releaseglobally.md)
  Releases the receiver’s resources in the pasteboard server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/general)*