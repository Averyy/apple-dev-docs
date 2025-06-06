# init(rulerView:markerLocation:image:imageOrigin:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated ruler marker, associating it with (but not adding it to) a specified ruler view and assigning the attributes provided.

**Availability**:
- macOS ?+

## Declaration

```swift
init(rulerView ruler: NSRulerView, markerLocation location: CGFloat, image: NSImage, imageOrigin: NSPoint)
```

#### Return Value

An initialized ruler marker object.

#### Discussion

The image used to draw the marker must be appropriate for the orientation of the ruler. Markers may need to look different on a horizontal ruler than on a vertical ruler, and the ruler view neither scales nor rotates the images.

To add the new ruler marker to `aRulerView`, use either of NSRulerView’s [`addMarker(_:)`](nsrulerview/addmarker(_:).md) or [`trackMarker(_:withMouseEvent:)`](nsrulerview/trackmarker(_:withmouseevent:).md) methods. [`addMarker(_:)`](nsrulerview/addmarker(_:).md) immediately puts the marker on the ruler, while [`trackMarker(_:withMouseEvent:)`](nsrulerview/trackmarker(_:withmouseevent:).md) allows the client view to intercede in the addition and placement of the marker.

A new ruler marker can be moved on its ruler view, but not removed. Use [`isMovable`](nsrulermarker/ismovable.md) and [`isRemovable`](nsrulermarker/isremovable.md) to change these attributes. The new ruler marker also has no represented object; use [`representedObject`](nsrulermarker/representedobject.md) to set one.

This method is the designated initializer for the NSRulerMarker class.

## Parameters

- `ruler`: The ruler view with which to associate the ruler marker. This method raises an   if    is  .
- `location`: The x or y position of the marker in the client view’s coordinate system, depending on whether the ruler view is horizontal or vertical.
- `image`: The image displayed at the marker location. This method raises an   if   is  .
- `imageOrigin`: The point within the image positioned at the marker location, expressed in pixels relative to the lower-left corner of the image.

## See Also

- [var image: NSImage](nsrulermarker/image.md)
  The receiver’s image.
- [Ruler and Paragraph Style Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Rulers/Rulers.html#//apple_ref/doc/uid/10000089i)
- [var markerLocation: CGFloat](nsrulermarker/markerlocation.md)
  The location of the receiver in the coordinate system of the ruler view’s client view.
- [var imageOrigin: NSPoint](nsrulermarker/imageorigin.md)
  The point in the receiver’s image that is positioned at the receiver’s location on the ruler view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker/init(rulerview:markerlocation:image:imageorigin:))*