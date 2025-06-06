# reloadItems(at:)

**Framework**: AppKit  
**Kind**: method

Reloads the items at the specified indexes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
func reloadItems(at indexes: IndexSet)
```

#### Discussion

The scrubber makes requests for updated views from the data source and then animates their display.

## Parameters

- `indexes`: The indexes of the items to reload, provided in an index set ( ).

## See Also

- [func reloadData()](nsscrubber/reloaddata.md)
  Reloads the content of the entire scrubber, and deselects the currently selected item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/reloaditems(at:))*