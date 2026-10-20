# reloadItems(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reloads the items at the specified indexes.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func reloadItems(at indexes: IndexSet)
```

```objc
- (void) reloadItemsAtIndexes:(NSIndexSet *) indexes;
```

#### Discussion

The scrubber makes requests for updated views from the data source and then animates their display.

## Parameters

- `indexes`: The indexes of the items to reload, provided in an index set ([`IndexSet`](../../Foundation/indexset.md)).

## See Also

### Reloading content
- [func reloadData()](./reloaddata%28%29.md)
  Reloads the content of the entire scrubber, and deselects the currently selected item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/reloaditems(at:))*