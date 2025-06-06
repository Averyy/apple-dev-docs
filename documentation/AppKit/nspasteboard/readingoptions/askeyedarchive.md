# asKeyedArchive

**Framework**: AppKit  
**Kind**: property

An option to read data from the pasteboard and use it to initialize the object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var asKeyedArchive: NSPasteboard.ReadingOptions { get }
```

#### Discussion

AppKit initializes the object using its [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) method.

## See Also

- [static var asData: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/asdata.md)
  An option to read data from the pasteboard as-is and return it as a data object.
- [static var asString: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/asstring.md)
  An option to read data from the pasteboard and convert it to a string object.
- [static var asPropertyList: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/aspropertylist.md)
  An option to read data from the pasteboard and unserialize it as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptions/askeyedarchive)*