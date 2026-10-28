# clearContents()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Clears the existing contents of the pasteboard.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func clearContents() -> Int
```

```objc
- (NSInteger) clearContents;
```

## Return Value

The change count of the receiver.

## Discussion

Clears the existing contents of the pasteboard, preparing it for new contents. This is the first step in providing data on the pasteboard.

## See Also

### Writing data
- [func writeObjects([any NSPasteboardWriting]) -> Bool](./writeobjects%28_%29.md)
  Writes an array of objects to the receiver.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](./setdata%28_,fortype%29.md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](./setpropertylist%28_,fortype%29.md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](./setstring%28_,fortype%29.md)
  Sets the given string as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](./pasteboardtype.md)
  The supported pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/clearcontents())*