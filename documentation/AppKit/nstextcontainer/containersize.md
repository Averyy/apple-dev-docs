# containerSize

**Framework**: AppKit  
**Kind**: property

The size of the text container’s bounding rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
var containerSize: NSSize { get set }
```

## See Also

- [convenience init(containerSize: NSSize)](nstextcontainer/init(containersize:).md)
  Initializes a text container with a specified bounding rectangle.
- [func lineFragmentRect(forProposedRect: NSRect, sweepDirection: NSLineSweepDirection, movementDirection: NSLineMovementDirection, remaining: NSRectPointer?) -> NSRect](nstextcontainer/linefragmentrect(forproposedrect:sweepdirection:movementdirection:remaining:).md)
  Calculates and returns the longest rectangle available in the proposed rectangle for displaying text.
- [func contains(NSPoint) -> Bool](nstextcontainer/contains(_:).md)
  Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/containersize)*