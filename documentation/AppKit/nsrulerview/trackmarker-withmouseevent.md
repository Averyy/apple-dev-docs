# trackMarker(_:withMouseEvent:)

**Framework**: AppKit  
**Kind**: method

Tracks the mouse to add `aMarker` based on the initial mouse-down or mouse-dragged event `theEvent`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func trackMarker(_ marker: NSRulerMarker, withMouseEvent event: NSEvent) -> Bool
```

#### Discussion

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the receiver adds `aMarker`, [`false`](https://developer.apple.com/documentation/swift/false) if it doesn’t. This method works by sending [`trackMouse(with:adding:)`](nsrulermarker/trackmouse(with:adding:).md) to `aMarker` with `theEvent` and [`true`](https://developer.apple.com/documentation/swift/true) as arguments.

An application typically invokes this method in one of two cases. In the simpler case, the client view can implement [`NSRulerView`](nsrulerview.md) to invoke this method when the user presses the mouse button while the cursor is in the NSRulerView’s ruler area. This technique is appropriate when it’s clear what kind of marker will be added by clicking the ruler area. The second, more general, case involves the application providing a palette of different kinds of markers that can be dragged onto the ruler, from the ruler’s accessory view or from some other place. With this technique the palette tracks the cursor until it enters the ruler view, at which time it hands over control to the ruler view by invoking [`trackMarker(_:withMouseEvent:)`](nsrulerview/trackmarker(_:withmouseevent:).md).

## See Also

- [var markers: [NSRulerMarker]?](nsrulerview/markers.md)
  The receiver’s ruler markers to `markers`, removing any existing ruler markers and not consulting with the client view about the new markers.
- [func addMarker(NSRulerMarker)](nsrulerview/addmarker(_:).md)
  Adds `aMarker` to the receiver, without consulting the client view for approval.
- [func removeMarker(NSRulerMarker)](nsrulerview/removemarker(_:).md)
  Removes `aMarker` from the receiver, without consulting the client view for approval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/trackmarker(_:withmouseevent:))*