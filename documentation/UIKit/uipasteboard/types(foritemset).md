# types(forItemSet:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of representation types for each specified pasteboard item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func types(forItemSet itemSet: IndexSet?) -> [[String]]?
```

```objc
- (NSArray<NSArray<NSString *> *> *) pasteboardTypesForItemSet:(NSIndexSet *) itemSet;
```

#### Return Value

An array of arrays, with each inner array holding the representation types for a particular pasteboard item.

## Parameters

- `itemSet`: An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in `nil` to request all pasteboard items.

## See Also

### Related Documentation
- [var numberOfItems: Int](./numberofitems.md)
  The number of items for the pasteboard.
### Determining types of pasteboard items
- [var types: [String]](./types.md)
  The types of the first item on the pasteboard.
- [func contains(pasteboardTypes: [String]) -> Bool](./contains%28pasteboardtypes%29.md)
  Returns whether the pasteboard holds data of the specified representation type.
- [func contains(pasteboardTypes: [String], inItemSet: IndexSet?) -> Bool](./contains%28pasteboardtypes,initemset%29.md)
  Returns whether the specified pasteboard items contain data of the given representation types.
- [func itemSet(withPasteboardTypes: [String]) -> IndexSet?](./itemset%28withpasteboardtypes%29.md)
  Returns an index set identifying pasteboard items having the specified representation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/types(foritemset:))*