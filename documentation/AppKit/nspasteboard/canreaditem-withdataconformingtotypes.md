# canReadItem(withDataConformingToTypes:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func canReadItem(withDataConformingToTypes types: [String]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver contains any items that conform to the UTIs specified in `types`, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `types`: An array of   objects containing UTIs.

## See Also

- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](nspasteboard/readobjects(forclasses:options:).md)
  Reads from the receiver objects that best match the specified array of classes.
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](nspasteboard/availabletype(from:).md)
  Scans the specified types for a type that the receiver supports.
- [func canReadObject(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> Bool](nspasteboard/canreadobject(forclasses:options:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.
- [var types: [NSPasteboard.PasteboardType]?](nspasteboard/types.md)
  An array of the receiver’s supported data types.
- [class func types(filterableTo: NSPasteboard.PasteboardType) -> [NSPasteboard.PasteboardType]](nspasteboard/types(filterableto:).md)
  Returns the data types that can be converted to the specified type using the available filter services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/canreaditem(withdataconformingtotypes:))*