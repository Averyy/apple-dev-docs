# asString

**Framework**: AppKit  
**Kind**: property

An option to read data from the pasteboard and convert it to a string object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var asString: NSPasteboard.ReadingOptions { get }
```

#### Discussion

AppKit puts the data in an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object.

## See Also

- [static var asData: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/asdata.md)
  An option to read data from the pasteboard as-is and return it as a data object.
- [static var asPropertyList: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/aspropertylist.md)
  An option to read data from the pasteboard and unserialize it as a property list.
- [static var asKeyedArchive: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/askeyedarchive.md)
  An option to read data from the pasteboard and use it to initialize the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptions/asstring)*