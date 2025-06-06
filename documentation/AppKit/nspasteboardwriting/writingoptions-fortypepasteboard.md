# writingOptions(forType:pasteboard:)

**Framework**: AppKit  
**Kind**: method

Returns options for writing data of a specified type to a given pasteboard.

**Availability**:
- macOS 10.6+

## Declaration

```swift
optional func writingOptions(forType type: NSPasteboard.PasteboardType, pasteboard: NSPasteboard) -> NSPasteboard.WritingOptions
```

#### Return Value

Options for writing data of type type to `pasteboard`. Return `0` for no options, or a value given in [`Pasteboard Writing Options`](pasteboard-writing-options.md).

#### Discussion

Do not perform other pasteboard operations in the method implementation.

## Parameters

- `type`: One of the types the receiver supports for writing (one of the UTIs returned by its implementation of  ).
- `pasteboard`: You can use this argument to provide different options based on the pasteboard name, if you need to.

## See Also

- [func writableTypes(for: NSPasteboard) -> [NSPasteboard.PasteboardType]](nspasteboardwriting/writabletypes(for:).md)
  Returns an array of UTI strings of data types the receiver can write to a given pasteboard.
- [NSPasteboard.WritingOptions](nspasteboard/writingoptions.md)
  Type to specify options for writing to a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardwriting/writingoptions(fortype:pasteboard:))*