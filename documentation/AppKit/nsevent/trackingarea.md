# trackingArea

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tracking area for the event.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var trackingArea: NSTrackingArea? { get }
```

```objc
@property (strong, readonly, nullable) NSTrackingArea * trackingArea;
```

#### Discussion

If you access this property on an event object that is not a mouse-tracking event — that is, its event type isn’t [`NSMouseEntered`](../nsmouseentered.md), [`NSMouseExited`](../nsmouseexited.md), or [`NSCursorUpdate`](../nscursorupdate.md) —AppKit raises an [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md).

If the event corresponds to a tracking rectangle installed with the [`addTrackingRect(_:owner:userData:assumeInside:)`](../nsview/addtrackingrect%28_,owner,userdata,assumeinside%29.md) method of [`NSView`](../nsview.md), the value of this property is `nil`. The [`trackingNumber`](./trackingnumber.md) property contains either an [`NSTrackingArea`](../nstrackingarea.md) object or [`NSView.TrackingRectTag`](../nsview/trackingrecttag.md), depending on how AppKit generated the event.

## See Also

### Getting tracking area information
- [var eventNumber: Int](./eventnumber.md)
  The counter value of the latest mouse or tracking-rectangle event object.
- [var trackingNumber: Int](./trackingnumber.md)
  The identifier of a mouse-tracking event.
- [var userData: UnsafeMutableRawPointer?](./userdata.md)
  The data associated with a mouse-tracking event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/trackingarea)*