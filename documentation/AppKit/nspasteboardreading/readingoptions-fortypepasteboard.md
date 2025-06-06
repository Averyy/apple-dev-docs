# readingOptions(forType:pasteboard:)

**Framework**: AppKit  
**Kind**: method

Returns options for reading data of a specified type from a given pasteboard.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional static func readingOptions(forType type: NSPasteboard.PasteboardType, pasteboard: NSPasteboard) -> NSPasteboard.ReadingOptions
```

#### Return Value

Options for reading data of `type` from `pasteboard`. For a list of valid values, see [`NSPasteboard.ReadingOptions`](nspasteboard/readingoptions.md).

#### Discussion

Do not perform other pasteboard operations in this method implementation.

## Parameters

- `type`: A UTI supported by instances of the receiver for reading (one of the types returned by  ).
- `pasteboard`: You can use the pasteboard argument to provide return different based on the pasteboard name, should you need to do so.

## See Also

- [static func readableTypes(for: NSPasteboard) -> [NSPasteboard.PasteboardType]](nspasteboardreading/readabletypes(for:).md)
  Returns an array of uniform type identifier strings of data types the receiver can read from the pasteboard and initialize from.
- [NSPasteboard.ReadingOptions](nspasteboard/readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardreading/readingoptions(fortype:pasteboard:))*