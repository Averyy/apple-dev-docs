# itemNumber(in:at:)

**Framework**: Foundation  
**Kind**: method

Returns the index of the item at the specified location within the list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func itemNumber(in list: NSTextList, at location: Int) -> Int
```

#### Return Value

Returns the index within the list.

## Parameters

- `list`: The text list.
- `location`: The location of the item.

## See Also

- [func range(of: NSTextBlock, at: Int) -> NSRange](nsattributedstring/range(of:at:)-1wrcp.md)
  Returns the range of the individual text block that contains the specified location.
- [func range(of: NSTextList, at: Int) -> NSRange](nsattributedstring/range(of:at:)-6um0x.md)
  Returns the range of the specified text list that contains the specified location.
- [func range(of: NSTextTable, at: Int) -> NSRange](nsattributedstring/range(of:at:)-3fevu.md)
  Returns the range of the specified text table that contains the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/itemnumber(in:at:))*