# checkSpaceForParts()

**Framework**: AppKit  
**Kind**: method

Checks to see if there is enough room in the receiver to display the knob and buttons.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func checkSpaceForParts()
```

#### Discussion

The  [`usableParts`](nsscroller/usableparts-swift.property.md) property contains the state calculated by this method. You should never need to invoke this method; it’s invoked automatically whenever the scroller’s size changes.

## See Also

- [func rect(for: NSScroller.Part) -> NSRect](nsscroller/rect(for:).md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
- [func testPart(NSPoint) -> NSScroller.Part](nsscroller/testpart(_:).md)
  Returns the part that would be hit by a mouse-down event at `aPoint` (expressed in the window’s coordinate system).
- [var usableParts: NSScroller.UsableParts](nsscroller/usableparts-swift.property.md)
  A value that indicates which parts of the receiver are displayed and usable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/checkspaceforparts())*