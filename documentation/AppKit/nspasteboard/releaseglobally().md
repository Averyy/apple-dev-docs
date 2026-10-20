# releaseGlobally()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Releases the receiver’s resources in the pasteboard server.

**Availability**:
- macOS

## Declaration

```swift
func releaseGlobally()
```

```objc
- (void) releaseGlobally;
```

#### Discussion

After this method is invoked, no other application can use the receiver.

> ❗ **Important**:  Although you must call this method to release a temporary, privately named pasteboard to avoid leaks, you should never call it on a standard pasteboard.

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
- [NSPasteboard.Name](./name-swift.struct.md)
  Constants that represent the standard pasteboard names.
- [class func withUniqueName() -> NSPasteboard](./withuniquename%28%29.md)
  Creates and returns a new pasteboard with a name that is guaranteed to be unique with respect to other pasteboards in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/releaseglobally())*