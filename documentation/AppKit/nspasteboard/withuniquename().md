# withUniqueName()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a new pasteboard with a name that is guaranteed to be unique with respect to other pasteboards in the system.

**Availability**:
- macOS

## Declaration

```swift
class func withUniqueName() -> NSPasteboard
```

```objc
+ (NSPasteboard *) pasteboardWithUniqueName;
```

## Return Value

The new pasteboard object.

## Discussion

This method is useful for apps that implement their own interprocess communication using pasteboards. Because the lifetime of a unique pasteboard is not related to the lifetime of the creating app, you must release a unique pasteboard by calling [`releaseGlobally()`](./releaseglobally%28%29.md) to avoid possible leaks.

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
- [func releaseGlobally()](./releaseglobally%28%29.md)
  Releases the receiver’s resources in the pasteboard server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/withuniquename())*