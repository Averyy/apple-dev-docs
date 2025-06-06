# range(of:at:)

**Framework**: Foundation  
**Kind**: method

Returns the range of the specified text table that contains the specified location.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func range(of table: NSTextTable, at location: Int) -> NSRange
```

#### Return Value

Returns the range of `table` that contains `location`.

## Parameters

- `table`: The text table.
- `location`: The location.

## See Also

- [func itemNumber(in: NSTextList, at: Int) -> Int](nsattributedstring/itemnumber(in:at:).md)
  Returns the index of the item at the specified location within the list.
- [func range(of: NSTextBlock, at: Int) -> NSRange](nsattributedstring/range(of:at:)-1wrcp.md)
  Returns the range of the individual text block that contains the specified location.
- [func range(of: NSTextList, at: Int) -> NSRange](nsattributedstring/range(of:at:)-6um0x.md)
  Returns the range of the specified text list that contains the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/range(of:at:)-3fevu)*