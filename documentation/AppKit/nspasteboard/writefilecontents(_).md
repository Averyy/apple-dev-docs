# writeFileContents(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the contents of the specified file to the pasteboard.

**Availability**:
- macOS

## Declaration

```swift
func writeFileContents(_ filename: String) -> Bool
```

```objc
- (BOOL) writeFileContents:(NSString *) filename;
```

## Return Value

[`true`](../../Swift/true.md) if the data was successfully written, otherwise [`false`](../../Swift/false.md).

## Discussion

Writes the contents of the file `filename` to the receiver and declares the data to be of type `NSFileContentsPboardType` and also of a type appropriate for the file’s extension (as returned by the `NSCreateFileContentsPboardType` function when passed the files extension), if it has one.

## Parameters

- `filename`: The name of the file to write to the pasteboard.

## See Also

### Related Documentation
- [func readFileContentsType(NSPasteboard.PasteboardType?, toFile: String) -> String?](./readfilecontentstype%28_,tofile%29.md)
  Reads data representing a file’s contents from the receiver and writes it to the specified file.
### Writing data (macOS 10.5 and earlier)
- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](./declaretypes%28_,owner%29.md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
- [func addTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](./addtypes%28_,owner%29.md)
  Adds promises for the specified types to the first pasteboard item.
- [func write(FileWrapper) -> Bool](./write%28_%29.md)
  Writes the serialized contents of the specified file wrapper to the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/writefilecontents(_:))*