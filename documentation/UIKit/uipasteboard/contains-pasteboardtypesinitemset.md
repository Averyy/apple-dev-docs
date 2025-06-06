# contains(pasteboardTypes:inItemSet:)

**Framework**: UIKit  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the pasteboard items identified by `itemSet` have data corresponding to the representation types specified by `pasteboardTypes`; otherwise, returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `pasteboardTypes`: An array of strings, with each string identifying a representation type. Typically you use UTIs as pasteboard types.
- `itemSet`: An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in   to request all pasteboard items.

## See Also

- [var numberOfItems: Int](uipasteboard/numberofitems.md)
  The number of items for the pasteboard.
- [var types: [String]](uipasteboard/types.md)
  The types of the first item on the pasteboard.
- [func types(forItemSet: IndexSet?) -> [[String]]?](uipasteboard/types(foritemset:).md)
  Returns an array of representation types for each specified pasteboard item.
- [func contains(pasteboardTypes: [String]) -> Bool](uipasteboard/contains(pasteboardtypes:).md)
  Returns whether the pasteboard holds data of the specified representation type.
- [func itemSet(withPasteboardTypes: [String]) -> IndexSet?](uipasteboard/itemset(withpasteboardtypes:).md)
  Returns an index set identifying pasteboard items having the specified representation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/contains(pasteboardtypes:initemset:))*