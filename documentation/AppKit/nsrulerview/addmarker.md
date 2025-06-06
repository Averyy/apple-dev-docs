# addMarker(_:)

**Framework**: AppKit  
**Kind**: method

Adds `aMarker` to the receiver, without consulting the client view for approval.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addMarker(_ marker: NSRulerMarker)
```

#### Discussion

Raises an `NSInternalInconsistencyException` if the receiver has no client view.

## See Also

- [var markers: [NSRulerMarker]?](nsrulerview/markers.md)
  The receiver’s ruler markers to `markers`, removing any existing ruler markers and not consulting with the client view about the new markers.
- [func removeMarker(NSRulerMarker)](nsrulerview/removemarker(_:).md)
  Removes `aMarker` from the receiver, without consulting the client view for approval.
- [func trackMarker(NSRulerMarker, withMouseEvent: NSEvent) -> Bool](nsrulerview/trackmarker(_:withmouseevent:).md)
  Tracks the mouse to add `aMarker` based on the initial mouse-down or mouse-dragged event `theEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/addmarker(_:))*