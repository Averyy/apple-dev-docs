# indexPath(forItemIdentifier:)

**Framework**: AppKit  
**Kind**: method

Returns an index path for the item with the specified identifier in the collection view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func indexPath(forItemIdentifier identifier: Any) -> IndexPath?
```

#### Return Value

The item’s index path, or `nil` if no item is found with the provided item identifier.

#### Discussion

This method is a constant time operation, O(1), which means you can look up an index path from its corresponding item identifier with no significant overhead.

## Parameters

- `identifier`: The identifier of the item in the collection view.

## See Also

- [func itemIdentifier(for: IndexPath) -> Any?](nscollectionviewdiffabledatasourcereference/itemidentifier(for:).md)
  Returns an identifier for the item at the specified index path in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasourcereference/indexpath(foritemidentifier:))*