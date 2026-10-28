# init(byFilteringData:ofType:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new pasteboard object that supplies the specified data in as many types as possible based on the available filter services.

**Availability**:
- macOS

## Declaration

```swift
init(byFilteringData data: Data, ofType type: NSPasteboard.PasteboardType)
```

```objc
+ (NSPasteboard *) pasteboardByFilteringData:(NSData *) data ofType:(NSPasteboardType) type;
```

## Return Value

The new pasteboard object.

## Discussion

The returned pasteboard also declares data of the supplied `type`.

No filter service is invoked until the data is actually requested, so invoking this method is reasonably inexpensive.

## Parameters

- `data`: The data to be placed on the pasteboard.
- `type`: The type of data in the `data` parameter.

## See Also

### Creating and releasing a pasteboard
- [class var general: NSPasteboard](./general.md)
  The shared pasteboard object to use for general content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/init(byfilteringdata:oftype:))*