# moveItem(at:to:)

**Framework**: AppKit  
**Kind**: method

Moves an item from one index to another in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func moveItem(at oldIndex: Int, to newIndex: Int)
```

## Parameters

- `oldIndex`: The index of the item that you want to move.
- `newIndex`: The index of the item’s new location.

## See Also

- [func insertItems(at: IndexSet)](nsscrubber/insertitems(at:).md)
  Inserts new items at the specified indexes into the scrubber.
- [func removeItems(at: IndexSet)](nsscrubber/removeitems(at:).md)
  Removes the items at the specified indexes from the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/moveitem(at:to:))*