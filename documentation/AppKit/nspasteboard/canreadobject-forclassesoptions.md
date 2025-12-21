# canReadObject(forClasses:options:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func canReadObject(forClasses classArray: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver contains any items that can be represented as an instance of a class specified in `classArray`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `classArray`: Classes in the array must conform to the   protocol.
- `options`: A dictionary that specifies options to refine the search for pasteboard items, for example to restrict the search to file URLs with particular content types. For valid dictionary keys, see  .

## See Also

- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](nspasteboard/readobjects(forclasses:options:).md)
  Reads from the receiver objects that best match the specified array of classes.
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](nspasteboard/availabletype(from:).md)
  Scans the specified types for a type that the receiver supports.
- [func canReadItem(withDataConformingToTypes: [String]) -> Bool](nspasteboard/canreaditem(withdataconformingtotypes:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.
- [var types: [NSPasteboard.PasteboardType]?](nspasteboard/types.md)
  An array of the receiver’s supported data types.
- [class func types(filterableTo: NSPasteboard.PasteboardType) -> [NSPasteboard.PasteboardType]](nspasteboard/types(filterableto:).md)
  Returns the data types that can be converted to the specified type using the available filter services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/canreadobject(forclasses:options:))*