# releaseGlobally()

**Framework**: AppKit  
**Kind**: method

Releases the receiver’s resources in the pasteboard server.

**Availability**:
- macOS ?+

## Declaration

```swift
func releaseGlobally()
```

#### Discussion

After this method is invoked, no other application can use the receiver.

> ❗ **Important**:  Although you must call this method to release a temporary, privately named pasteboard to avoid leaks, you should never call it on a standard pasteboard.

 Although you must call this method to release a temporary, privately named pasteboard to avoid leaks, you should never call it on a standard pasteboard.

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
- [class func withUniqueName() -> NSPasteboard](nspasteboard/withuniquename.md)
  Creates and returns a new pasteboard with a name that is guaranteed to be unique with respect to other pasteboards in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/releaseglobally())*