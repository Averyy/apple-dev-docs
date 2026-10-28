# contains(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```swift
func contains(_ point: NSPoint) -> Bool
```

```objc
- (BOOL) containsPoint:(NSPoint) point;
```

## Return Value

[`true`](../../Swift/true.md) if `aPoint` lies within the receiver’s region or on the region’s edge—not simply within its bounding rectangle—[`false`](../../Swift/false.md) otherwise.

## Discussion

For example, if the receiver defines a donut shape and `aPoint` lies in the hole, this method returns [`false`](../../Swift/false.md). This method can be used for hit testing of mouse events.

The default [`NSTextContainer`](../nstextcontainer.md) implementation merely checks that `aPoint` lies within its bounding rectangle.

## Parameters

- `point`: The point in question.

## See Also

### Deprecated
- [convenience init(containerSize: NSSize)](./init%28containersize%29.md)
  Initializes a text container with a specified bounding rectangle.
- [func lineFragmentRect(forProposedRect: NSRect, sweepDirection: NSLineSweepDirection, movementDirection: NSLineMovementDirection, remaining: NSRectPointer?) -> NSRect](./linefragmentrect%28forproposedrect,sweepdirection,movementdirection,remaining%29.md)
  Calculates and returns the longest rectangle available in the proposed rectangle for displaying text.
- [var containerSize: NSSize](./containersize.md)
  The size of the text container’s bounding rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/contains(_:))*