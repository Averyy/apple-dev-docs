# writeObjects(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes an array of objects to the receiver.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func writeObjects(_ objects: [any NSPasteboardWriting]) -> Bool
```

```objc
- (BOOL) writeObjects:(NSArray<id<NSPasteboardWriting>> *) objects;
```

#### Return Value

[`true`](../../Swift/true.md) if the array was successfully added, otherwise [`false`](../../Swift/false.md).

## Parameters

- `objects`: An array of objects that implement the [`NSPasteboardWriting`](../nspasteboardwriting.md) protocol (including instances of [`NSPasteboardItem`](../nspasteboarditem.md)).

## See Also

### Writing data
- [func clearContents() -> Int](./clearcontents%28%29.md)
  Clears the existing contents of the pasteboard.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](./setdata%28_,fortype%29.md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](./setpropertylist%28_,fortype%29.md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](./setstring%28_,fortype%29.md)
  Sets the given string as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](./pasteboardtype.md)
  The supported pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/writeobjects(_:))*