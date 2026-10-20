# removeItems(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the items at the specified indexes from the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func removeItems(at indexes: IndexSet)
```

```objc
- (void) removeItemsAtIndexes:(NSIndexSet *) indexes;
```

## Parameters

- `indexes`: An index set ([`IndexSet`](../../Foundation/indexset.md)) of the indexes of the items to remove.

## See Also

### Inserting, moving, and deleting items
- [func insertItems(at: IndexSet)](./insertitems%28at%29.md)
  Inserts new items at the specified indexes into the scrubber.
- [func moveItem(at: Int, to: Int)](./moveitem%28at,to%29.md)
  Moves an item from one index to another in the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/removeitems(at:))*