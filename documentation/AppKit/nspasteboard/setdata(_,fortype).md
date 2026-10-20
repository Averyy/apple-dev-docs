# setData(_:forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the data as the representation for the specified type for the first item on the receiver.

**Availability**:
- macOS

## Declaration

```swift
func setData(_ data: Data?, forType dataType: NSPasteboard.PasteboardType) -> Bool
```

```objc
- (BOOL) setData:(NSData *) data forType:(NSPasteboardType) dataType;
```

#### Return Value

[`true`](../../Swift/true.md) if the data was written successfully, otherwise [`false`](../../Swift/false.md) if ownership of the pasteboard has changed. Any other error raises an `NSPasteboardCommunicationException`.

## Parameters

- `data`: The data to write to the pasteboard.
- `dataType`: The type of data in the `data` parameter. The type must have been declared by a previous [`declareTypes(_:owner:)`](./declaretypes%28_,owner%29.md) message.

## See Also

### Related Documentation
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](./data%28fortype%29.md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
### Writing data
- [func clearContents() -> Int](./clearcontents%28%29.md)
  Clears the existing contents of the pasteboard.
- [func writeObjects([any NSPasteboardWriting]) -> Bool](./writeobjects%28_%29.md)
  Writes an array of objects to the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](./setpropertylist%28_,fortype%29.md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](./setstring%28_,fortype%29.md)
  Sets the given string as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](./pasteboardtype.md)
  The supported pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/setdata(_:fortype:))*