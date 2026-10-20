# types

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of uniform type identifier strings of the data types that the receiver supports.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var types: [NSPasteboard.PasteboardType] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * types;
```

## See Also

### Getting types
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](./availabletype%28from%29.md)
  Returns from a given array of types the first type within the pasteboard item, according to the ordering of types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/types)*