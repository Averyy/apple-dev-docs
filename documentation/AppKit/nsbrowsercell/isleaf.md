# isLeaf

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the browser cell is a leaf or a branch cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isLeaf: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the browser cell is a leaf cell.

A branch `NSBrowserCell` has an image near its right edge indicating that more, hierarchically related information is available; when the user selects the cell, the `NSBrowser` displays a new column of `NSBrowserCell` objects. A leaf `NSBrowserCell` has no image, indicating that the user has reached a terminal piece of information; it doesn’t point to additional information.

## See Also

- [func reset()](nsbrowsercell/reset.md)
  Unhighlights the receiver and unsets its state.
- [func set()](nsbrowsercell/set.md)
  Highlights the receiver and sets its state.
- [var isLoaded: Bool](nsbrowsercell/isloaded.md)
  A Boolean that indicates whether the cell is ready to display.
- [func highlightColor(in: NSView) -> NSColor?](nsbrowsercell/highlightcolor(in:).md)
  Returns the highlight color that the receiver wants to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/isleaf)*