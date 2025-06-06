# withUniqueName()

**Framework**: AppKit  
**Kind**: method

Creates and returns a new pasteboard with a name that is guaranteed to be unique with respect to other pasteboards in the system.

**Availability**:
- macOS ?+

## Declaration

```swift
class func withUniqueName() -> NSPasteboard
```

#### Return Value

The new pasteboard object.

#### Discussion

This method is useful for apps that implement their own interprocess communication using pasteboards. Because the lifetime of a unique pasteboard is not related to the lifetime of the creating app, you must release a unique pasteboard by calling [`releaseGlobally()`](nspasteboard/releaseglobally().md) to avoid possible leaks.

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
- [NSPasteboard.Name](nspasteboard/name-swift.struct.md)
  Constants that represent the standard pasteboard names.
- [func releaseGlobally()](nspasteboard/releaseglobally.md)
  Releases the receiver’s resources in the pasteboard server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/withuniquename())*