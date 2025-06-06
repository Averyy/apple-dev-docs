# highlightColor(in:)

**Framework**: AppKit  
**Kind**: method

Returns the highlight color that the receiver wants to display.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func highlightColor(in controlView: NSView) -> NSColor?
```

#### Return Value

The highlight color.

## Parameters

- `controlView`: The view for which to return the highlight color.

## See Also

- [func reset()](nsbrowsercell/reset.md)
  Unhighlights the receiver and unsets its state.
- [func set()](nsbrowsercell/set.md)
  Highlights the receiver and sets its state.
- [var isLeaf: Bool](nsbrowsercell/isleaf.md)
  A Boolean that indicates whether the browser cell is a leaf or a branch cell.
- [var isLoaded: Bool](nsbrowsercell/isloaded.md)
  A Boolean that indicates whether the cell is ready to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/highlightcolor(in:))*