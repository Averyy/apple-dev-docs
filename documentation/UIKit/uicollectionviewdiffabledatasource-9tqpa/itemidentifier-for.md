# itemIdentifier(for:)

**Framework**: UIKit  
**Kind**: method

Returns an identifier for the item at the specified index path in the collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func itemIdentifier(for indexPath: IndexPath) -> ItemIdentifierType?
```

#### Return Value

The item’s identifier, or `nil` if no item is found at the provided index path.

#### Discussion

This method is a constant time operation, O(1), which means you can look up an item identifier from its corresponding index path with no significant overhead.

## Parameters

- `indexPath`: The index path of the item in the collection view.

## See Also

- [func indexPath(for: ItemIdentifierType) -> IndexPath?](uicollectionviewdiffabledatasource-9tqpa/indexpath(for:).md)
  Returns an index path for the item with the specified identifier in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/itemidentifier(for:))*