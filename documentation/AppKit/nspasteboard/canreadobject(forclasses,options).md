# canReadObject(forClasses:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func canReadObject(forClasses classArray: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]? = nil) -> Bool
```

```objc
- (BOOL) canReadObjectForClasses:(NSArray<Class> *) classArray options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver contains any items that can be represented as an instance of a class specified in `classArray`, otherwise [`false`](../../Swift/false.md).

## Parameters

- `classArray`: An array of class objects.

  Classes in the array must conform to the [`NSPasteboardReading`](../nspasteboardreading.md) protocol.
- `options`: A dictionary that specifies options to refine the search for pasteboard items, for example to restrict the search to file URLs with particular content types. For valid dictionary keys, see `Pasteboard Reading Options`.

## See Also

### Related Documentation
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](./readobjects%28forclasses,options%29.md)
  Reads from the receiver objects that best match the specified array of classes.
### Validating contents
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](./availabletype%28from%29.md)
  Scans the specified types for a type that the receiver supports.
- [func canReadItem(withDataConformingToTypes: [String]) -> Bool](./canreaditem%28withdataconformingtotypes%29.md)
  Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.
- [var types: [NSPasteboard.PasteboardType]?](./types.md)
  An array of the receiver’s supported data types.
- [class func types(filterableTo: NSPasteboard.PasteboardType) -> [NSPasteboard.PasteboardType]](./types%28filterableto%29.md)
  Returns the data types that can be converted to the specified type using the available filter services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/canreadobject(forclasses:options:))*