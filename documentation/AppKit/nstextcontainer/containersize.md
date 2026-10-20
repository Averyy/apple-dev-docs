# containerSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The size of the text container’s bounding rectangle.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use [`size`](./size.md) instead.

## Declaration

```swift
var containerSize: NSSize { get set }
```

```objc
@property NSSize containerSize;
```

## See Also

### Deprecated
- [convenience init(containerSize: NSSize)](./init%28containersize%29.md)
  Initializes a text container with a specified bounding rectangle.
- [func lineFragmentRect(forProposedRect: NSRect, sweepDirection: NSLineSweepDirection, movementDirection: NSLineMovementDirection, remaining: NSRectPointer?) -> NSRect](./linefragmentrect%28forproposedrect,sweepdirection,movementdirection,remaining%29.md)
  Calculates and returns the longest rectangle available in the proposed rectangle for displaying text.
- [func contains(NSPoint) -> Bool](./contains%28_%29.md)
  Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/containersize)*