# types(forItemSet:)

**Framework**: UIKit  
**Kind**: method

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

#### Return Value

An array of arrays, with each inner array holding the representation types for a particular pasteboard item.

## Parameters

- `itemSet`: An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in   to request all pasteboard items.

## See Also

- [var numberOfItems: Int](uipasteboard/numberofitems.md)
  The number of items for the pasteboard.
- [var types: [String]](uipasteboard/types.md)
  The types of the first item on the pasteboard.
- [func contains(pasteboardTypes: [String]) -> Bool](uipasteboard/contains(pasteboardtypes:).md)
  Returns whether the pasteboard holds data of the specified representation type.
- [func contains(pasteboardTypes: [String], inItemSet: IndexSet?) -> Bool](uipasteboard/contains(pasteboardtypes:initemset:).md)
  Returns whether the specified pasteboard items contain data of the given representation types.
- [func itemSet(withPasteboardTypes: [String]) -> IndexSet?](uipasteboard/itemset(withpasteboardtypes:).md)
  Returns an index set identifying pasteboard items having the specified representation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/types(foritemset:))*