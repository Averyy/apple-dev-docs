# select(_:byExtendingSelection:)

**Framework**: Quartz  
**Kind**: method

Invoked to select the specified files, extending the selection if specified.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func select(_ indexes: IndexSet!, byExtendingSelection extend: Bool)
```

## Parameters

- `indexes`: The indexes of the files to select.
- `extend`: [`true`](https://developer.apple.com/documentation/Swift/true) if the selection should be extended, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func selectedIndexes() -> IndexSet!](ikcameradeviceview/selectedindexes.md)
  The selected indexes of the camera files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/select(_:byextendingselection:))*