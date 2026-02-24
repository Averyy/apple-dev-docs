# init(pasteboardPropertyList:ofType:)

**Framework**: AppKit  
**Kind**: init  
**Required**: Yes

Initializes an instance with a property list object and a type string.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(pasteboardPropertyList propertyList: Any, ofType type: NSPasteboard.PasteboardType)
```

#### Return Value

An object initialized using the data in `propertyList`.

#### Discussion

This method is considered optional because, if [`readableTypes(for:)`](nspasteboardreading/readabletypes(for:).md) returns just a single type, and that type uses the [`asKeyedArchive`](nspasteboard/readingoptions/askeyedarchive.md) reading option, then instances are initialized using [`init(coder:)`](https://developer.apple.com/documentation/Foundation/NSCoding/init(coder:)) instead of this method.

## Parameters

- `propertyList`: A property list containing data to initialize the receiver. By default, the property list object is an instance of `NSData`. If you implement [`readingOptions(forType:pasteboard:)`](nspasteboardreading/readingoptions(fortype:pasteboard:).md) and specify an option other than [`asData`](nspasteboard/readingoptions/asdata.md), the `propertyList` may be any other property list object.
- `type`: A UTI supported by the receiver for reading (one of the types returned by [`readableTypes(for:)`](nspasteboardreading/readabletypes(for:).md)).

## See Also

- [Drag and Drop](drag-and-drop.md)
  Support the direct manipulation of your app’s content using drag and drop.
- [class NSPasteboard](nspasteboard.md)
  An object that transfers data to and from the pasteboard server.
- [Services Functions](services-functions.md)
  Configure the contents of your app’s Services menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardreading/init(pasteboardpropertylist:oftype:))*