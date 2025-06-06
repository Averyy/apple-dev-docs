# asData

**Framework**: AppKit  
**Kind**: property

An option to read data from the pasteboard as-is and return it as a data object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var asData: NSPasteboard.ReadingOptions { get }
```

#### Discussion

This is the default value. AppKit returns the data in an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object.

## See Also

- [static var asString: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/asstring.md)
  An option to read data from the pasteboard and convert it to a string object.
- [static var asPropertyList: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/aspropertylist.md)
  An option to read data from the pasteboard and unserialize it as a property list.
- [static var asKeyedArchive: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/askeyedarchive.md)
  An option to read data from the pasteboard and use it to initialize the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptions/asdata)*