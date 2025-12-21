# outlineView(_:shouldReorderColumn:toColumn:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate to allow or prohibit the specified column to be dragged to a new location.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldReorderColumn columnIndex: Int, toColumn newColumnIndex: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the column reordering should be allowed, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

When a column is initially dragged by the user, the delegate is first called with a `newColumnIndex` value of `-1`. Returning [`false`](https://developer.apple.com/documentation/Swift/false) will disallow that column from being reordered at all. Returning [`true`](https://developer.apple.com/documentation/Swift/true) allows it to be reordered, and the delegate will be called again when the column reaches a new location.

The actual `NSTableColumn` instance can be retrieved from the [`tableColumns`](nstableview/tablecolumns.md) array.

If this method is not implemented, all columns are considered reorderable.

## Parameters

- `outlineView`: The outline view that sent the message.
- `columnIndex`: The index of the column being dragged.
- `newColumnIndex`: The proposed target index of the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldreordercolumn:tocolumn:))*