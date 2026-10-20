# init(containerSize:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a text container with a specified bounding rectangle.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use [`init(size:)`](./init%28size%29.md) instead.

## Declaration

```swift
convenience init(containerSize aContainerSize: NSSize)
```

```objc
- (instancetype) initWithContainerSize:(NSSize) aContainerSize;
```

#### Return Value

The newly initialized text container.

#### Discussion

The new text container must be added to an [`NSLayoutManager`](../nslayoutmanager.md) object before it can be used. The text container must also have an [`NSTextView`](../nstextview.md) object set for text to be displayed. This method is the designated initializer for the `NSTextContainer` class.

## Parameters

- `aContainerSize`: The size of the text container’s bounding rectangle.

## See Also

### Deprecated
- [func lineFragmentRect(forProposedRect: NSRect, sweepDirection: NSLineSweepDirection, movementDirection: NSLineMovementDirection, remaining: NSRectPointer?) -> NSRect](./linefragmentrect%28forproposedrect,sweepdirection,movementdirection,remaining%29.md)
  Calculates and returns the longest rectangle available in the proposed rectangle for displaying text.
- [func contains(NSPoint) -> Bool](./contains%28_%29.md)
  Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle.
- [var containerSize: NSSize](./containersize.md)
  The size of the text container’s bounding rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/init(containersize:))*