# usableParts

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates which parts of the receiver are displayed and usable.

**Availability**:
- macOS

## Declaration

```swift
var usableParts: NSScroller.UsableParts { get }
```

```objc
@property (readonly) NSUsableScrollerParts usableParts;
```

## Discussion

See [`NSScroller.UsableParts`](./usableparts-swift.enum.md) for a list of possible values.

## See Also

### Related Documentation
- [var arrowsPosition: NSScroller.ArrowPosition](./arrowsposition.md)
  The location of the scroll buttons within the scroller, as described in [`NSScroller.ArrowPosition`](./arrowposition.md).
### Calculating Layout
- [func rect(for: NSScroller.Part) -> NSRect](./rect%28for%29.md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
- [func testPart(NSPoint) -> NSScroller.Part](./testpart%28_%29.md)
  Returns the part that would be hit by a mouse-down event at `aPoint` (expressed in the window’s coordinate system).
- [func checkSpaceForParts()](./checkspaceforparts%28%29.md)
  Checks to see if there is enough room in the receiver to display the knob and buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/usableparts-swift.property)*