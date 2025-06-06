# init(containerSize:)

**Framework**: AppKit  
**Kind**: init

Initializes a text container with a specified bounding rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
convenience init(containerSize aContainerSize: NSSize)
```

#### Return Value

The newly initialized text container.

#### Discussion

The new text container must be added to an [`NSLayoutManager`](nslayoutmanager.md) object before it can be used. The text container must also have an [`NSTextView`](nstextview.md) object set for text to be displayed. This method is the designated initializer for the `NSTextContainer` class.

## Parameters

- `aContainerSize`: The size of the text container’s bounding rectangle.

## See Also

- [func lineFragmentRect(forProposedRect: NSRect, sweepDirection: NSLineSweepDirection, movementDirection: NSLineMovementDirection, remaining: NSRectPointer?) -> NSRect](nstextcontainer/linefragmentrect(forproposedrect:sweepdirection:movementdirection:remaining:).md)
  Calculates and returns the longest rectangle available in the proposed rectangle for displaying text.
- [func contains(NSPoint) -> Bool](nstextcontainer/contains(_:).md)
  Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle.
- [var containerSize: NSSize](nstextcontainer/containersize.md)
  The size of the text container’s bounding rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/init(containersize:))*