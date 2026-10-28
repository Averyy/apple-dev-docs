# types

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of the receiver’s supported data types.

**Availability**:
- macOS

## Declaration

```swift
var types: [NSPasteboard.PasteboardType]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSString *> * types;
```

## Discussion

The [`types`](./types.md) array is an array of [`NSString`](../../Foundation/nsstring.md) objects containing the union of the types of data declared for all the pasteboard items on the receiver. The returned types are listed in the order they were declared. It’s a good idea to check the value of [`types`](./types.md) (or call [`availableType(from:)`](./availabletype%28from%29.md)) before reading any data from an `NSPasteboard` object. If you need to see if a type in the [`types`](./types.md) array matches a type string you have stored locally, use the [`isEqual(to:)`](../../Foundation/nsstring/isequal%28to%29.md) method to perform the comparison.

## See Also

### Related Documentation
- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](./declaretypes%28_,owner%29.md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](./data%28fortype%29.md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
### Validating contents
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](./availabletype%28from%29.md)
  Scans the specified types for a type that the receiver supports.
- [func canReadItem(withDataConformingToTypes: [String]) -> Bool](./canreaditem%28withdataconformingtotypes%29.md)
  Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.
- [func canReadObject(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> Bool](./canreadobject%28forclasses,options%29.md)
  Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.
- [class func types(filterableTo: NSPasteboard.PasteboardType) -> [NSPasteboard.PasteboardType]](./types%28filterableto%29.md)
  Returns the data types that can be converted to the specified type using the available filter services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/types)*