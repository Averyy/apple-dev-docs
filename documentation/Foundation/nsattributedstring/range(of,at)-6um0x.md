# range(of:at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the range of the specified text list that contains the specified location.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func range(of list: NSTextList, at location: Int) -> NSRange
```

```objc
- (NSRange) rangeOfTextList:(NSTextList *) list atIndex:(NSUInteger) location;
```

## Return Value

The range of the given text list containing the location.

## Parameters

- `list`: The text list.
- `location`: The location in the text list.

## See Also

### Calculating ranges for common elements
- [func itemNumber(in: NSTextList, at: Int) -> Int](./itemnumber%28in,at%29.md)
  Returns the index of the item at the specified location within the list.
- [func range(of: NSTextBlock, at: Int) -> NSRange](./range%28of,at%29-1wrcp.md)
  Returns the range of the individual text block that contains the specified location.
- [func range(of: NSTextTable, at: Int) -> NSRange](./range%28of,at%29-3fevu.md)
  Returns the range of the specified text table that contains the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/range(of:at:)-6um0x)*