# asData

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An option to read data from the pasteboard as-is and return it as a data object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var asData: NSPasteboard.ReadingOptions { get }
```

```c
NSPasteboardReadingAsData
```

#### Discussion

This is the default value. AppKit returns the data in an [`NSData`](../../../Foundation/nsdata.md) object.

## See Also

### Options
- [static var asString: NSPasteboard.ReadingOptions](./asstring.md)
  An option to read data from the pasteboard and convert it to a string object.
- [static var asPropertyList: NSPasteboard.ReadingOptions](./aspropertylist.md)
  An option to read data from the pasteboard and unserialize it as a property list.
- [static var asKeyedArchive: NSPasteboard.ReadingOptions](./askeyedarchive.md)
  An option to read data from the pasteboard and use it to initialize the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptions/asdata)*