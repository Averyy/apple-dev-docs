# cell(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the entry at the specified index.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
func cell(at index: Int) -> Any!
```

```objc
- (id) cellAtIndex:(NSInteger) index;
```

#### Return Value

The form cell object at the specified index.

## Parameters

- `index`: The index of the desired entry.

## See Also

### Getting Cells and Indices
- [func indexOfCell(withTag: Int) -> Int](./indexofcell%28withtag%29.md)
  Returns the index of the entry whose tag is `tag`.
- [func indexOfSelectedItem() -> Int](./indexofselecteditem%28%29.md)
  Returns the index of the selected entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/cell(at:))*