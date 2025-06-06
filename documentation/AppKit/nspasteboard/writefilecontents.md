# writeFileContents(_:)

**Framework**: AppKit  
**Kind**: method

Writes the contents of the specified file to the pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
func writeFileContents(_ filename: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the data was successfully written, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Writes the contents of the file `filename` to the receiver and declares the data to be of type `NSFileContentsPboardType` and also of a type appropriate for the file’s extension (as returned by the `NSCreateFileContentsPboardType` function when passed the files extension), if it has one.

## Parameters

- `filename`: The name of the file to write to the pasteboard.

## See Also

- [func readFileContentsType(NSPasteboard.PasteboardType?, toFile: String) -> String?](nspasteboard/readfilecontentstype(_:tofile:).md)
  Reads data representing a file’s contents from the receiver and writes it to the specified file.
- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](nspasteboard/declaretypes(_:owner:).md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
- [func addTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](nspasteboard/addtypes(_:owner:).md)
  Adds promises for the specified types to the first pasteboard item.
- [func write(FileWrapper) -> Bool](nspasteboard/write(_:).md)
  Writes the serialized contents of the specified file wrapper to the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/writefilecontents(_:))*