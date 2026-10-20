# indexOfCell(withTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the entry whose tag is `tag`.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
func indexOfCell(withTag tag: Int) -> Int
```

```objc
- (NSInteger) indexOfCellWithTag:(NSInteger) tag;
```

## Parameters

- `tag`: The tag of the desired entry.

## See Also

### Related Documentation
- [var tag: Int](../nscell/tag.md)
  A tag for identifying the cell.
### Getting Cells and Indices
- [func indexOfSelectedItem() -> Int](./indexofselecteditem%28%29.md)
  Returns the index of the selected entry.
- [func cell(at: Int) -> Any!](./cell%28at%29.md)
  Returns the entry at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/indexofcell(withtag:))*