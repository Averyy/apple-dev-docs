# frameResize(position:directions:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the cursor for resizing a rectangular frame from the specified edge or corner.

**Availability**:
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
class func frameResize(position: NSCursor.FrameResizePosition, directions: NSCursor.FrameResizeDirection.Set) -> NSCursor
```

## Return Value

The frame-resize cursor for the specified position and directions.

## Discussion

The `position` parameter selects the edge or corner of the frame, and the `directions` parameter is a set that specifies whether that edge or corner can resize outward, away from the center of the frame, inward, toward the center, or both. The cursor changes to show the allowed directions.

The following table shows the cursor for each position and set of directions. The `.all` column applies when `directions` contains both `.inward` and `.outward`:

| Position | `.outward` | `.inward` | `.all` |
| --- | --- | --- | --- |
| `.top` | ![bottom edge, inward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-north@2x.png) | ![bottom edge, outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-south@2x.png) | ![bottom edge, inward and outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-north-south@2x.png) |
| `.bottom` | ![bottom edge, outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-south@2x.png) | ![bottom edge, inward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-north@2x.png) | ![bottom edge, inward and outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-north-south@2x.png) |
| `.left` | ![right edge, inward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-west@2x.png) | ![right edge, outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-east@2x.png) | ![right edge, inward and outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-east-west@2x.png) |
| `.right` | ![right edge, outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-east@2x.png) | ![right edge, inward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-west@2x.png) | ![right edge, inward and outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-east-west@2x.png) |
| `.topLeft` | ![bottom-right corner, inward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northwest@2x.png) | ![bottom-right corner, outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-southeast@2x.png) | ![bottom-right corner, inward and outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northwest-southeast@2x.png) |
| `.topRight` | ![bottom-left corner, inward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northeast@2x.png) | ![bottom-left corner, outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-southwest@2x.png) | ![bottom-left corner, inward and outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northeast-southwest@2x.png) |
| `.bottomLeft` | ![bottom-left corner, outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-southwest@2x.png) | ![bottom-left corner, inward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northeast@2x.png) | ![bottom-left corner, inward and outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northeast-southwest@2x.png) |
| `.bottomRight` | ![bottom-right corner, outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-southeast@2x.png) | ![bottom-right corner, inward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northwest@2x.png) | ![bottom-right corner, inward and outward](https://developer.apple.com/tutorials/images/com.apple.appkit/nscursor-northwest-southeast@2x.png) |

## Parameters

- `position`: The position along the perimeter of a rectangular frame (its edges and corners) from which it resizes.
- `directions`: The directions in which a rectangular frame can resize. This must not be empty.

## See Also

### Retrieving cursor instances
- [class var current: NSCursor](./current.md)
  Returns the application’s current cursor.
- [class var arrow: NSCursor](./arrow.md)
  Returns the default cursor, the arrow cursor.
- [class var contextualMenu: NSCursor](./contextualmenu.md)
  Returns the contextual menu system cursor.
- [class var closedHand: NSCursor](./closedhand.md)
  Returns the closed-hand system cursor.
- [class var crosshair: NSCursor](./crosshair.md)
  Returns the cross-hair system cursor.
- [class var disappearingItem: NSCursor](./disappearingitem.md)
  Returns a cursor indicating that the current operation will result in a disappearing item.
- [class var dragCopy: NSCursor](./dragcopy.md)
  Returns a cursor indicating that the current operation will result in a copy action.
- [class var dragLink: NSCursor](./draglink.md)
  Returns a cursor indicating that the current operation will result in a link action.
- [class var iBeam: NSCursor](./ibeam.md)
  Returns a cursor that looks like a capital I with a tiny crossbeam at its middle.
- [class var iBeamCursorForVerticalLayout: NSCursor](./ibeamcursorforverticallayout.md)
  Returns the cursor for editing vertical layout text.
- [class var openHand: NSCursor](./openhand.md)
  Returns the open-hand system cursor.
- [class var operationNotAllowed: NSCursor](./operationnotallowed.md)
  Returns the operation not allowed cursor.
- [class var pointingHand: NSCursor](./pointinghand.md)
  Returns the pointing-hand system cursor.
- [class var zoomIn: NSCursor](./zoomin.md)
  Returns the zoom-in cursor.
- [class var zoomOut: NSCursor](./zoomout.md)
  Returns the zoom-out cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/frameresize(position:directions:))*