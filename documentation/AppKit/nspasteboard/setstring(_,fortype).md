# setString(_:forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the given string as the representation for the specified type for the first item on the receiver.

**Availability**:
- macOS

## Declaration

```swift
func setString(_ string: String, forType dataType: NSPasteboard.PasteboardType) -> Bool
```

```objc
- (BOOL) setString:(NSString *) string forType:(NSPasteboardType) dataType;
```

## Mentions

- [Supporting Writing Tools via the pasteboard](../supporting-writing-tools-via-the-pasteboard.md)

## Return Value

[`true`](../../Swift/true.md) if the data was written successfully, otherwise [`false`](../../Swift/false.md) if ownership of the pasteboard has changed. Any other error raises an `NSPasteboardCommunicationException`.

## Discussion

This method invokes [`setData(_:forType:)`](./setdata%28_,fortype%29.md) to perform the write.

## Parameters

- `string`: The string to write to the pasteboard.
- `dataType`: The type of string data. The type must have been declared by a previous [`declareTypes(_:owner:)`](./declaretypes%28_,owner%29.md) message.

## See Also

### Related Documentation
- [func string(forType: NSPasteboard.PasteboardType) -> String?](./string%28fortype%29.md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.
### Writing data
- [func clearContents() -> Int](./clearcontents%28%29.md)
  Clears the existing contents of the pasteboard.
- [func writeObjects([any NSPasteboardWriting]) -> Bool](./writeobjects%28_%29.md)
  Writes an array of objects to the receiver.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](./setdata%28_,fortype%29.md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](./setpropertylist%28_,fortype%29.md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](./pasteboardtype.md)
  The supported pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/setstring(_:fortype:))*