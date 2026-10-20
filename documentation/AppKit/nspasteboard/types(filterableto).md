# types(filterableTo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the data types that can be converted to the specified type using the available filter services.

**Availability**:
- macOS

## Declaration

```swift
class func types(filterableTo type: NSPasteboard.PasteboardType) -> [NSPasteboard.PasteboardType]
```

```objc
+ (NSArray<NSString *> *) typesFilterableTo:(NSPasteboardType) type;
```

#### Return Value

An array of `NSString` objects containing the types that can be converted to the target data type.

#### Discussion

The array also contains the original type.

## Parameters

- `type`: The target data type.

## See Also

### Validating contents
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](./availabletype%28from%29.md)
  Scans the specified types for a type that the receiver supports.
- [func canReadItem(withDataConformingToTypes: [String]) -> Bool](./canreaditem%28withdataconformingtotypes%29.md)
  Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.
- [func canReadObject(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> Bool](./canreadobject%28forclasses,options%29.md)
  Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.
- [var types: [NSPasteboard.PasteboardType]?](./types.md)
  An array of the receiver’s supported data types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/types(filterableto:))*