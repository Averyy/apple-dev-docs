# indexOfSelectedItem()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the selected entry.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
func indexOfSelectedItem() -> Int
```

```objc
- (NSInteger) indexOfSelectedItem;
```

#### Return Value

The index of the selected entry, or `-1` if no entry is selected.

## See Also

### Getting Cells and Indices
- [func indexOfCell(withTag: Int) -> Int](./indexofcell%28withtag%29.md)
  Returns the index of the entry whose tag is `tag`.
- [func cell(at: Int) -> Any!](./cell%28at%29.md)
  Returns the entry at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/indexofselecteditem())*