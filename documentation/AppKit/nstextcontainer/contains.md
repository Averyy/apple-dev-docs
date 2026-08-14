# contains(_:)

**Framework**: AppKit  
**Kind**: method

Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func contains(_ point: NSPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `aPoint` lies within the receiver’s region or on the region’s edge—not simply within its bounding rectangle—[`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

For example, if the receiver defines a donut shape and `aPoint` lies in the hole, this method returns [`false`](https://developer.apple.com/documentation/swift/false). This method can be used for hit testing of mouse events.

The default [`NSTextContainer`](nstextcontainer.md) implementation merely checks that `aPoint` lies within its bounding rectangle.

## Parameters

- `point`: The point in question.

## See Also

- [convenience init(containerSize: NSSize)](nstextcontainer/init(containersize:).md)
  Initializes a text container with a specified bounding rectangle.
- [func lineFragmentRect(forProposedRect: NSRect, sweepDirection: NSLineSweepDirection, movementDirection: NSLineMovementDirection, remaining: NSRectPointer?) -> NSRect](nstextcontainer/linefragmentrect(forproposedrect:sweepdirection:movementdirection:remaining:).md)
  Calculates and returns the longest rectangle available in the proposed rectangle for displaying text.
- [var containerSize: NSSize](nstextcontainer/containersize.md)
  The size of the text container’s bounding rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/contains(_:))*