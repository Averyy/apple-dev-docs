# general

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The shared pasteboard object to use for general content.

**Availability**:
- macOS

## Declaration

```swift
class var general: NSPasteboard { get }
```

```objc
@property (class, strong, readonly) NSPasteboard * generalPasteboard;
```

#### Return Value

The general pasteboard.

#### Discussion

Invokes [`init(name:)`](./init%28name%29.md) to obtain the pasteboard.

## See Also

### Related Documentation
- [Drag and Drop](../drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [class NSPasteboard](../nspasteboard.md)
  An object that transfers data to and from the pasteboard server.
- [Services Functions](../services-functions.md)
  Configure the contents of your app’s Services menu.
### Creating and releasing a pasteboard
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
- [func releaseGlobally()](./releaseglobally%28%29.md)
  Releases the receiver’s resources in the pasteboard server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/general)*