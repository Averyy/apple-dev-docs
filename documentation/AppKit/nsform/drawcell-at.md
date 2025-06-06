# drawCell(at:)

**Framework**: AppKit  
**Kind**: method

Displays the entry at the specified index.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func drawCell(at index: Int)
```

#### Discussion

Because this method is called automatically whenever a cell needs drawing, you never need to invoke it explicitly. It is included in the API so you can override it if you subclass `NSFormCell`.

## Parameters

- `index`: The index of the entry to draw.

## See Also

- [func indexOfCell(withTag: Int) -> Int](nsform/indexofcell(withtag:).md)
  Returns the index of the entry whose tag is `tag`.
- [func indexOfSelectedItem() -> Int](nsform/indexofselecteditem.md)
  Returns the index of the selected entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/drawcell(at:))*