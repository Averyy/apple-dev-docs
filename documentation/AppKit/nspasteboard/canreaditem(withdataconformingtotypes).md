# canReadItem(withDataConformingToTypes:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func canReadItem(withDataConformingToTypes types: [String]) -> Bool
```

```objc
- (BOOL) canReadItemWithDataConformingToTypes:(NSArray<NSString *> *) types;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver contains any items that conform to the UTIs specified in `types`, otherwise [`false`](../../Swift/false.md).

## Parameters

- `types`: An array of `NSString` objects containing UTIs.

## See Also

### Related Documentation
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](./readobjects%28forclasses,options%29.md)
  Reads from the receiver objects that best match the specified array of classes.
### Validating contents
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](./availabletype%28from%29.md)
  Scans the specified types for a type that the receiver supports.
- [func canReadObject(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> Bool](./canreadobject%28forclasses,options%29.md)
  Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.
- [var types: [NSPasteboard.PasteboardType]?](./types.md)
  An array of the receiver’s supported data types.
- [class func types(filterableTo: NSPasteboard.PasteboardType) -> [NSPasteboard.PasteboardType]](./types%28filterableto%29.md)
  Returns the data types that can be converted to the specified type using the available filter services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/canreaditem(withdataconformingtotypes:))*