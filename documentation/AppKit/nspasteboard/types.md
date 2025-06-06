# types

**Framework**: AppKit  
**Kind**: property

An array of the receiver’s supported data types.

**Availability**:
- macOS ?+

## Declaration

```swift
var types: [NSPasteboard.PasteboardType]? { get }
```

#### Discussion

The [`types`](nspasteboard/types.md) array is an array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects containing the union of the types of data declared for all the pasteboard items on the receiver. The returned types are listed in the order they were declared. It’s a good idea to check the value of [`types`](nspasteboard/types.md) (or call [`availableType(from:)`](nspasteboard/availabletype(from:).md)) before reading any data from an `NSPasteboard` object. If you need to see if a type in the [`types`](nspasteboard/types.md) array matches a type string you have stored locally, use the [`isEqual(to:)`](https://developer.apple.com/documentation/foundation/nsstring/1407803-isequal) method to perform the comparison.

## See Also

- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](nspasteboard/declaretypes(_:owner:).md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](nspasteboard/data(fortype:).md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](nspasteboard/availabletype(from:).md)
  Scans the specified types for a type that the receiver supports.
- [func canReadItem(withDataConformingToTypes: [String]) -> Bool](nspasteboard/canreaditem(withdataconformingtotypes:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.
- [func canReadObject(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> Bool](nspasteboard/canreadobject(forclasses:options:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.
- [class func types(filterableTo: NSPasteboard.PasteboardType) -> [NSPasteboard.PasteboardType]](nspasteboard/types(filterableto:).md)
  Returns the data types that can be converted to the specified type using the available filter services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/types)*