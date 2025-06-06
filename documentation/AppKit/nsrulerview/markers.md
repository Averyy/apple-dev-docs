# markers

**Framework**: AppKit  
**Kind**: property

The receiver’s ruler markers to `markers`, removing any existing ruler markers and not consulting with the client view about the new markers.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var markers: [NSRulerMarker]? { get set }
```

#### Discussion

`markers` can be `nil` or empty to remove all ruler markers. Raises an `NSInternalInconsistencyException` if `markers` is not `nil` and the receiver has no client view.

## See Also

- [var markerLocation: CGFloat](nsrulermarker/markerlocation.md)
  The location of the receiver in the coordinate system of the ruler view’s client view.
- [func addMarker(NSRulerMarker)](nsrulerview/addmarker(_:).md)
  Adds `aMarker` to the receiver, without consulting the client view for approval.
- [func removeMarker(NSRulerMarker)](nsrulerview/removemarker(_:).md)
  Removes `aMarker` from the receiver, without consulting the client view for approval.
- [func trackMarker(NSRulerMarker, withMouseEvent: NSEvent) -> Bool](nsrulerview/trackmarker(_:withmouseevent:).md)
  Tracks the mouse to add `aMarker` based on the initial mouse-down or mouse-dragged event `theEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/markers)*