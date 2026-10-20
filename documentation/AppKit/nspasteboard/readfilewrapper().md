# readFileWrapper()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reads data representing a file’s contents from the receiver and returns it as a file wrapper.

**Availability**:
- macOS

## Declaration

```swift
func readFileWrapper() -> FileWrapper?
```

```objc
- (NSFileWrapper *) readFileWrapper;
```

#### Return Value

A file wrapper containing the pasteboard data, or `nil` if the receiver contained no data of type `NSFileContentsPboardType`.

#### Discussion

In macOS 10.5 and earlier, the file contents pboard type allowed you to synthesize a pboard type for a file’s contents based on the file’s extension. In macOS 10.5 and later, using the UTI of a file to represent its contents now replaces this functionality.

## See Also

### Reading data (macOS 10.5 and earlier)
- [func readFileContentsType(NSPasteboard.PasteboardType?, toFile: String) -> String?](./readfilecontentstype%28_,tofile%29.md)
  Reads data representing a file’s contents from the receiver and writes it to the specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readfilewrapper())*