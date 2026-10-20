# drawCell(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the entry at the specified index.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSTextField directly instead, and consider NSStackView for layout assistance

## Declaration

```swift
func drawCell(at index: Int)
```

```objc
- (void) drawCellAtIndex:(NSInteger) index;
```

#### Discussion

Because this method is called automatically whenever a cell needs drawing, you never need to invoke it explicitly. It is included in the API so you can override it if you subclass `NSFormCell`.

## Parameters

- `index`: The index of the entry to draw.

## See Also

### Related Documentation
- [func indexOfCell(withTag: Int) -> Int](./indexofcell%28withtag%29.md)
  Returns the index of the entry whose tag is `tag`.
- [func indexOfSelectedItem() -> Int](./indexofselecteditem%28%29.md)
  Returns the index of the selected entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsform/drawcell(at:))*