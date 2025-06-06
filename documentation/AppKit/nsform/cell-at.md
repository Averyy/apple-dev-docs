# cell(at:)

**Framework**: AppKit  
**Kind**: method

Returns the entry at the specified index.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func cell(at index: Int) -> Any!
```

#### Return Value

The form cell object at the specified index.

## Parameters

- `index`: The index of the desired entry.

## See Also

- [func indexOfCell(withTag: Int) -> Int](nsform/indexofcell(withtag:).md)
  Returns the index of the entry whose tag is `tag`.
- [func indexOfSelectedItem() -> Int](nsform/indexofselecteditem.md)
  Returns the index of the selected entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/cell(at:))*