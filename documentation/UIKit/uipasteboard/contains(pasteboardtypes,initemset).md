# contains(pasteboardTypes:inItemSet:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the specified pasteboard items contain data of the given representation types.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func contains(pasteboardTypes: [String], inItemSet itemSet: IndexSet?) -> Bool
```

```objc
- (BOOL) containsPasteboardTypes:(NSArray<NSString *> *) pasteboardTypes inItemSet:(NSIndexSet *) itemSet;
```

## Return Value

[`true`](../../Swift/true.md) if the pasteboard items identified by `itemSet` have data corresponding to the representation types specified by `pasteboardTypes`; otherwise, returns [`false`](../../Swift/false.md).

## Parameters

- `pasteboardTypes`: An array of strings, with each string identifying a representation type. Typically you use UTIs as pasteboard types.
- `itemSet`: An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in `nil` to request all pasteboard items.

## See Also

### Related Documentation
- [var numberOfItems: Int](./numberofitems.md)
  The number of items for the pasteboard.
### Determining types of pasteboard items
- [var types: [String]](./types.md)
  The types of the first item on the pasteboard.
- [func types(forItemSet: IndexSet?) -> [[String]]?](./types%28foritemset%29.md)
  Returns an array of representation types for each specified pasteboard item.
- [func contains(pasteboardTypes: [String]) -> Bool](./contains%28pasteboardtypes%29.md)
  Returns whether the pasteboard holds data of the specified representation type.
- [func itemSet(withPasteboardTypes: [String]) -> IndexSet?](./itemset%28withpasteboardtypes%29.md)
  Returns an index set identifying pasteboard items having the specified representation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/contains(pasteboardtypes:initemset:))*