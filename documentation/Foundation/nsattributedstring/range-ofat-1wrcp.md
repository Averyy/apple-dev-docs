# range(of:at:)

**Framework**: Foundation  
**Kind**: method

Returns the range of the individual text block that contains the specified location.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func range(of block: NSTextBlock, at location: Int) -> NSRange
```

#### Return Value

The range of the text block containing the location.

## Parameters

- `block`: The text block.
- `location`: The location in the text block.

## See Also

- [func itemNumber(in: NSTextList, at: Int) -> Int](nsattributedstring/itemnumber(in:at:).md)
  Returns the index of the item at the specified location within the list.
- [func range(of: NSTextList, at: Int) -> NSRange](nsattributedstring/range(of:at:)-6um0x.md)
  Returns the range of the specified text list that contains the specified location.
- [func range(of: NSTextTable, at: Int) -> NSRange](nsattributedstring/range(of:at:)-3fevu.md)
  Returns the range of the specified text table that contains the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/range(of:at:)-1wrcp)*