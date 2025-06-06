# itemSet(withPasteboardTypes:)

**Framework**: UIKit  
**Kind**: method

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

#### Return Value

An index set with each integer positionally identifying a pasteboard item that has one of the representation types specified in `pasteboardTypes`.

#### Discussion

You can pass the index set returned in this method in a call to [`data(forPasteboardType:inItemSet:)`](uipasteboard/data(forpasteboardtype:initemset:).md) or [`values(forPasteboardType:inItemSet:)`](uipasteboard/values(forpasteboardtype:initemset:).md) to get the data in the indicated pasteboard items.

## Parameters

- `pasteboardTypes`: An array of strings, with each string identifying a representation type. Typically you use UTIs as pasteboard types.

## See Also

- [var numberOfItems: Int](uipasteboard/numberofitems.md)
  The number of items for the pasteboard.
- [var types: [String]](uipasteboard/types.md)
  The types of the first item on the pasteboard.
- [func types(forItemSet: IndexSet?) -> [[String]]?](uipasteboard/types(foritemset:).md)
  Returns an array of representation types for each specified pasteboard item.
- [func contains(pasteboardTypes: [String]) -> Bool](uipasteboard/contains(pasteboardtypes:).md)
  Returns whether the pasteboard holds data of the specified representation type.
- [func contains(pasteboardTypes: [String], inItemSet: IndexSet?) -> Bool](uipasteboard/contains(pasteboardtypes:initemset:).md)
  Returns whether the specified pasteboard items contain data of the given representation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/itemset(withpasteboardtypes:))*