# row(forItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the row associated with a given item.

**Availability**:
- macOS

## Declaration

```swift
func row(forItem item: Any?) -> Int
```

```objc
- (NSInteger) rowForItem:(id) item;
```

## Return Value

The row associated with `item`, or `–1` if `item` is `nil` or cannot be found.

## Parameters

- `item`: An item in the receiver.

## See Also

### Converting Between Items and Rows
- [func item(atRow: Int) -> Any?](./item%28atrow%29.md)
  Returns the item associated with a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineview/row(foritem:))*