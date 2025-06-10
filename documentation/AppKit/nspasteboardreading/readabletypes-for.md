# readableTypes(for:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns an array of uniform type identifier strings of data types the receiver can read from the pasteboard and initialize from.

**Availability**:
- macOS ?+

## Declaration

```swift
static func readableTypes(for pasteboard: NSPasteboard) -> [NSPasteboard.PasteboardType]
```

#### Return Value

An array of uniform type identifier strings of data types instances that the receiver can read from the pasteboard and initialize from.

#### Discussion

By default, the system provides the data for a type to [`init(pasteboardPropertyList:ofType:)`](nsimage/init(pasteboardpropertylist:oftype:).md) as an instance of `NSData`. If you implement [`readingOptions(forType:pasteboard:)`](nspasteboardreading/readingoptions(fortype:pasteboard:).md) and specify a different option, the system converts the `NSData` object for a type to an `NSString` object or any other property list object.

##### Special Considerations

Don’t perform other pasteboard operations in the method implementation.

## Parameters

- `pasteboard`: A pasteboard. You can use the pasteboard argument to provide different types based on the pasteboard name, if you need to.

## See Also

- [static func readingOptions(forType: NSPasteboard.PasteboardType, pasteboard: NSPasteboard) -> NSPasteboard.ReadingOptions](nspasteboardreading/readingoptions(fortype:pasteboard:).md)
  Returns options for reading data of a specified type from a given pasteboard.
- [NSPasteboard.ReadingOptions](nspasteboard/readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardreading/readabletypes(for:))*