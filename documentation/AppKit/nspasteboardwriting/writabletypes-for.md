# writableTypes(for:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns an array of UTI strings of data types the receiver can write to a given pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
func writableTypes(for pasteboard: NSPasteboard) -> [NSPasteboard.PasteboardType]
```

#### Return Value

An array of UTI strings of data types the receiver can write to `pasteboard`.

#### Discussion

By default, data for the first returned type is put onto the pasteboard immediately, with the remaining types being promised.

To change the default behavior, implement -writingOptionsForType:pasteboard: and return [`promised`](nspasteboard/writingoptions/promised.md) to lazily provide data for types, return no option to provide the data for that type immediately.  Use the pasteboard argument to provide different types based on the pasteboard name, if desired.  Do not perform other pasteboard operations in the method implementation.

## Parameters

- `pasteboard`: You can use this argument to provide different options based on the pasteboard name, if you need to.

## See Also

- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [Pasteboard Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PasteboardGuide106/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008099)
- [Services Implementation Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SysServices/introduction.html#//apple_ref/doc/uid/10000101i)
- [func writingOptions(forType: NSPasteboard.PasteboardType, pasteboard: NSPasteboard) -> NSPasteboard.WritingOptions](nspasteboardwriting/writingoptions(fortype:pasteboard:).md)
  Returns options for writing data of a specified type to a given pasteboard.
- [NSPasteboard.WritingOptions](nspasteboard/writingoptions.md)
  Type to specify options for writing to a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardwriting/writabletypes(for:))*