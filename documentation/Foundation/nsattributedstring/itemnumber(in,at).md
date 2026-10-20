# itemNumber(in:at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the index of the item at the specified location within the list.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func itemNumber(in list: NSTextList, at location: Int) -> Int
```

```objc
- (NSInteger) itemNumberInTextList:(NSTextList *) list atIndex:(NSUInteger) location;
```

#### Return Value

Returns the index within the list.

## Parameters

- `list`: The text list.
- `location`: The location of the item.

## See Also

### Calculating ranges for common elements
- [func range(of: NSTextBlock, at: Int) -> NSRange](./range%28of,at%29-1wrcp.md)
  Returns the range of the individual text block that contains the specified location.
- [func range(of: NSTextList, at: Int) -> NSRange](./range%28of,at%29-6um0x.md)
  Returns the range of the specified text list that contains the specified location.
- [func range(of: NSTextTable, at: Int) -> NSRange](./range%28of,at%29-3fevu.md)
  Returns the range of the specified text table that contains the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/itemnumber(in:at:))*