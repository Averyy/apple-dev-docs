# readFileContentsType(_:toFile:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reads data representing a file’s contents from the receiver and writes it to the specified file.

**Availability**:
- macOS

## Declaration

```swift
func readFileContentsType(_ type: NSPasteboard.PasteboardType?, toFile filename: String) -> String?
```

```objc
- (NSString *) readFileContentsType:(NSPasteboardType) type toFile:(NSString *) filename;
```

## Return Value

The name of the file into which the data was actually written.

## Discussion

Data of any file contents type should only be read using this method. If data matching the specified type is not found on the pasteboard, data of type `NSFileContentsPboardType` is requested.

> **macOS 10.6 and later**:  In macOS 10.5 and earlier, the file contents pboard type allowed you to synthesize a pboard type for a file’s contents based on the file’s extension. In macOS 10.5 and later, using the UTI of a file to represent its contents now replaces this functionality.

### Special Considerations

You must send an [`availableType(from:)`](./availabletype%28from%29.md) or [`types`](./types.md) message before invoking [`readFileContentsType(_:toFile:)`](./readfilecontentstype%28_,tofile%29.md).

## Parameters

- `type`: The pasteboard data type to read. You should generally specify a value for this parameter. If you specify `nil`, the filename extension (in combination with the `NSCreateFileContentsPboardType` function) is used to determine the type.
- `filename`: The file to receive the pasteboard data.

## See Also

### Related Documentation
- [func writeFileContents(String) -> Bool](./writefilecontents%28_%29.md)
  Writes the contents of the specified file to the pasteboard.
### Reading data (macOS 10.5 and earlier)
- [func readFileWrapper() -> FileWrapper?](./readfilewrapper%28%29.md)
  Reads data representing a file’s contents from the receiver and returns it as a file wrapper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readfilecontentstype(_:tofile:))*