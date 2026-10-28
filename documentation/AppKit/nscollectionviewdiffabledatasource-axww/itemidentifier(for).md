# itemIdentifier(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an identifier for the item at the specified index path in the collection view.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
func itemIdentifier(for indexPath: IndexPath) -> ItemIdentifierType?
```

## Return Value

The item’s identifier, or `nil` if no item is found at the provided index path.

## Discussion

This method is a constant time operation, O(1), which means you can look up an item identifier from its corresponding index path with no significant overhead.

## Parameters

- `indexPath`: The index path of the item in the collection view.

## See Also

### Identifying Items
- [func indexPath(for: ItemIdentifierType) -> IndexPath?](./indexpath%28for%29.md)
  Returns an index path for the item with the specified identifier in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasource-axww/itemidentifier(for:))*