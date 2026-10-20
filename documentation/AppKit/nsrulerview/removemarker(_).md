# removeMarker(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes `aMarker` from the receiver, without consulting the client view for approval.

**Availability**:
- macOS

## Declaration

```swift
func removeMarker(_ marker: NSRulerMarker)
```

```objc
- (void) removeMarker:(NSRulerMarker *) marker;
```

## See Also

### Adding and removing markers
- [var markers: [NSRulerMarker]?](./markers.md)
  The receiver’s ruler markers to `markers`, removing any existing ruler markers and not consulting with the client view about the new markers.
- [func addMarker(NSRulerMarker)](./addmarker%28_%29.md)
  Adds `aMarker` to the receiver, without consulting the client view for approval.
- [func trackMarker(NSRulerMarker, withMouseEvent: NSEvent) -> Bool](./trackmarker%28_,withmouseevent%29.md)
  Tracks the mouse to add `aMarker` based on the initial mouse-down or mouse-dragged event `theEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/removemarker(_:))*