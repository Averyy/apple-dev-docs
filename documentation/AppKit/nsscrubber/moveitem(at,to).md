# moveItem(at:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves an item from one index to another in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func moveItem(at oldIndex: Int, to newIndex: Int)
```

```objc
- (void) moveItemAtIndex:(NSInteger) oldIndex toIndex:(NSInteger) newIndex;
```

## Parameters

- `oldIndex`: The index of the item that you want to move.
- `newIndex`: The index of the item’s new location.

## See Also

### Inserting, moving, and deleting items
- [func insertItems(at: IndexSet)](./insertitems%28at%29.md)
  Inserts new items at the specified indexes into the scrubber.
- [func removeItems(at: IndexSet)](./removeitems%28at%29.md)
  Removes the items at the specified indexes from the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/moveitem(at:to:))*