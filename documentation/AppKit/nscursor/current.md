# current

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the application’s current cursor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class var current: NSCursor { get }
```

```objc
@property (class, strong, readonly) NSCursor * currentCursor;
```

#### Return Value

The top cursor on the application’s cursor stack. This cursor may not be the visible cursor on the screen if a different application is currently active.

#### Discussion

The method only returns the cursor set by your application using `NSCursor` methods. It does not return cursors set by other applications or cursors set by your application using Carbon APIs.

## See Also

### Related Documentation
- [func mouseEntered(with: NSEvent)](./mouseentered%28with%29.md)
  Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.
- [func pop()](./pop%28%29-swift.method.md)
  Sends a [`pop()`](./pop%28%29-swift.type.method.md) message to the receiver’s class.
- [func push()](./push%28%29.md)
  Puts the receiver on top of the cursor stack and makes it the current cursor.
- [func set()](./set%28%29.md)
  Makes the receiver the current cursor.
- [func mouseExited(with: NSEvent)](./mouseexited%28with%29.md)
  Automatically sent to the receiver when the cursor exits a cursor rectangle owned by the receiver.
### Retrieving cursor instances
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
- [class var columnResize: NSCursor](./columnresize.md)
  Returns the cursor for resizing a column (vertical divider) in either direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/current)*