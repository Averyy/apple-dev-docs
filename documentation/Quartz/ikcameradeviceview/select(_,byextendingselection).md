# select(_:byExtendingSelection:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Invoked to select the specified files, extending the selection if specified.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func select(_ indexes: IndexSet!, byExtendingSelection extend: Bool)
```

```objc
- (void) selectIndexes:(NSIndexSet *) indexes byExtendingSelection:(BOOL) extend;
```

## Parameters

- `indexes`: The indexes of the files to select.
- `extend`: [`true`](../../Swift/true.md) if the selection should be extended, otherwise [`false`](../../Swift/false.md).

## See Also

### Selection Management
- [func selectedIndexes() -> IndexSet!](./selectedindexes%28%29.md)
  The selected indexes of the camera files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/select(_:byextendingselection:))*