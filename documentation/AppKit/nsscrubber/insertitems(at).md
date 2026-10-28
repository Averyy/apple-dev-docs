# insertItems(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts new items at the specified indexes into the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func insertItems(at indexes: IndexSet)
```

```objc
- (void) insertItemsAtIndexes:(NSIndexSet *) indexes;
```

## Discussion

The scrubber requests the view for each index from its data source.

## Parameters

- `indexes`: An index set ([`IndexSet`](../../Foundation/indexset.md)) of the indexes of the items to insert.

## See Also

### Inserting, moving, and deleting items
- [func moveItem(at: Int, to: Int)](./moveitem%28at,to%29.md)
  Moves an item from one index to another in the scrubber.
- [func removeItems(at: IndexSet)](./removeitems%28at%29.md)
  Removes the items at the specified indexes from the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/insertitems(at:))*