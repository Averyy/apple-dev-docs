# asKeyedArchive

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An option to read data from the pasteboard and use it to initialize the object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var asKeyedArchive: NSPasteboard.ReadingOptions { get }
```

```c
NSPasteboardReadingAsKeyedArchive
```

#### Discussion

AppKit initializes the object using its [`init(coder:)`](../../../Foundation/nscoding/init%28coder%29.md) method.

## See Also

### Options
- [static var asData: NSPasteboard.ReadingOptions](./asdata.md)
  An option to read data from the pasteboard as-is and return it as a data object.
- [static var asString: NSPasteboard.ReadingOptions](./asstring.md)
  An option to read data from the pasteboard and convert it to a string object.
- [static var asPropertyList: NSPasteboard.ReadingOptions](./aspropertylist.md)
  An option to read data from the pasteboard and unserialize it as a property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptions/askeyedarchive)*