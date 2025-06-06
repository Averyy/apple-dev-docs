# usableParts

**Framework**: AppKit  
**Kind**: property

A value that indicates which parts of the receiver are displayed and usable.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usableParts: NSScroller.UsableParts { get }
```

#### Discussion

See [`NSScroller.UsableParts`](nsscroller/usableparts-swift.enum.md) for a list of possible values.

## See Also

- [var arrowsPosition: NSScroller.ArrowPosition](nsscroller/arrowsposition.md)
  The location of the scroll buttons within the scroller, as described in [`NSScroller.ArrowPosition`](nsscroller/arrowposition.md).
- [func rect(for: NSScroller.Part) -> NSRect](nsscroller/rect(for:).md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
- [func testPart(NSPoint) -> NSScroller.Part](nsscroller/testpart(_:).md)
  Returns the part that would be hit by a mouse-down event at `aPoint` (expressed in the window’s coordinate system).
- [func checkSpaceForParts()](nsscroller/checkspaceforparts.md)
  Checks to see if there is enough room in the receiver to display the knob and buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/usableparts-swift.property)*