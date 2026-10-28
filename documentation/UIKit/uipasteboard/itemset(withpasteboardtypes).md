# itemSet(withPasteboardTypes:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns an index set identifying pasteboard items having the specified representation types.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func itemSet(withPasteboardTypes pasteboardTypes: [String]) -> IndexSet?
```

```objc
- (NSIndexSet *) itemSetWithPasteboardTypes:(NSArray<NSString *> *) pasteboardTypes;
```

## Return Value

An index set with each integer positionally identifying a pasteboard item that has one of the representation types specified in `pasteboardTypes`.

## Discussion

You can pass the index set returned in this method in a call to [`data(forPasteboardType:inItemSet:)`](./data%28forpasteboardtype,initemset%29.md) or [`values(forPasteboardType:inItemSet:)`](./values%28forpasteboardtype,initemset%29.md) to get the data in the indicated pasteboard items.

## Parameters

- `pasteboardTypes`: An array of strings, with each string identifying a representation type. Typically you use UTIs as pasteboard types.

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
- [func contains(pasteboardTypes: [String], inItemSet: IndexSet?) -> Bool](./contains%28pasteboardtypes,initemset%29.md)
  Returns whether the specified pasteboard items contain data of the given representation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/itemset(withpasteboardtypes:))*