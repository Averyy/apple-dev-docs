# types

**Framework**: AppKit  
**Kind**: property

An array of uniform type identifier strings of the data types that the receiver supports.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var types: [NSPasteboard.PasteboardType] { get }
```

## See Also

- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](nspasteboarditem/availabletype(from:).md)
  Returns from a given array of types the first type within the pasteboard item, according to the ordering of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/types)*