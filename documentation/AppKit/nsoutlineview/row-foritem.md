# row(forItem:)

**Framework**: AppKit  
**Kind**: method

Returns the row associated with a given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func row(forItem item: Any?) -> Int
```

#### Return Value

The row associated with `item`, or `–1` if `item` is `nil` or cannot be found.

## Parameters

- `item`: An item in the receiver.

## See Also

- [func item(atRow: Int) -> Any?](nsoutlineview/item(atrow:).md)
  Returns the item associated with a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/row(foritem:))*