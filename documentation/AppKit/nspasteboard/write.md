# write(_:)

**Framework**: AppKit  
**Kind**: method

Writes the serialized contents of the specified file wrapper to the pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
func write(_ wrapper: FileWrapper) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the data was successfully written, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Writes the serialized contents of the file wrapper `wrapper` to the receiver and declares the data to be of type `NSFileContentsPboardType` and also of a type appropriate for the file’s extension (as returned by the `NSCreateFileContentsPboardType` function when passed the files extension), if it has one. If `wrapper` does not have a preferred filename, this method raises an exception.

## Parameters

- `wrapper`: The file wrapper to write to the pasteboard.

## See Also

- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](nspasteboard/declaretypes(_:owner:).md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
- [func addTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](nspasteboard/addtypes(_:owner:).md)
  Adds promises for the specified types to the first pasteboard item.
- [func writeFileContents(String) -> Bool](nspasteboard/writefilecontents(_:).md)
  Writes the contents of the specified file to the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/write(_:))*