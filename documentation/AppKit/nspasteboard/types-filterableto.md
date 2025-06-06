# types(filterableTo:)

**Framework**: AppKit  
**Kind**: method

Returns the data types that can be converted to the specified type using the available filter services.

**Availability**:
- macOS ?+

## Declaration

```swift
class func types(filterableTo type: NSPasteboard.PasteboardType) -> [NSPasteboard.PasteboardType]
```

#### Return Value

An array of `NSString` objects containing the types that can be converted to the target data type.

#### Discussion

The array also contains the original type.

## Parameters

- `type`: The target data type.

## See Also

- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](nspasteboard/availabletype(from:).md)
  Scans the specified types for a type that the receiver supports.
- [func canReadItem(withDataConformingToTypes: [String]) -> Bool](nspasteboard/canreaditem(withdataconformingtotypes:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.
- [func canReadObject(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> Bool](nspasteboard/canreadobject(forclasses:options:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.
- [var types: [NSPasteboard.PasteboardType]?](nspasteboard/types.md)
  An array of the receiver’s supported data types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/types(filterableto:))*