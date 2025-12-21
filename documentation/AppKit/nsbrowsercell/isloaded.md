# isLoaded

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the cell is ready to display.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isLoaded: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the browser cell’s state has been set and the cell is ready to display.

## See Also

- [func reset()](nsbrowsercell/reset.md)
  Unhighlights the receiver and unsets its state.
- [func set()](nsbrowsercell/set.md)
  Highlights the receiver and sets its state.
- [var isLeaf: Bool](nsbrowsercell/isleaf.md)
  A Boolean that indicates whether the browser cell is a leaf or a branch cell.
- [func highlightColor(in: NSView) -> NSColor?](nsbrowsercell/highlightcolor(in:).md)
  Returns the highlight color that the receiver wants to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/isloaded)*