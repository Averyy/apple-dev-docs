# insertItems(at:)

**Framework**: AppKit  
**Kind**: method

Inserts new items at the specified indexes into the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func insertItems(at indexes: IndexSet)
```

#### Discussion

The scrubber requests the view for each index from its data source.

## Parameters

- `indexes`: An index set ( ) of the indexes of the items to insert.

## See Also

- [func moveItem(at: Int, to: Int)](nsscrubber/moveitem(at:to:).md)
  Moves an item from one index to another in the scrubber.
- [func removeItems(at: IndexSet)](nsscrubber/removeitems(at:).md)
  Removes the items at the specified indexes from the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/insertitems(at:))*