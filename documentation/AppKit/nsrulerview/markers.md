# markers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s ruler markers to `markers`, removing any existing ruler markers and not consulting with the client view about the new markers.

**Availability**:
- macOS

## Declaration

```swift
var markers: [NSRulerMarker]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSRulerMarker *> * markers;
```

## Discussion

`markers` can be `nil` or empty to remove all ruler markers. Raises an `NSInternalInconsistencyException` if `markers` is not `nil` and the receiver has no client view.

## See Also

### Related Documentation
- [var markerLocation: CGFloat](../nsrulermarker/markerlocation.md)
  The location of the receiver in the coordinate system of the ruler view’s client view.
### Adding and removing markers
- [func addMarker(NSRulerMarker)](./addmarker%28_%29.md)
  Adds `aMarker` to the receiver, without consulting the client view for approval.
- [func removeMarker(NSRulerMarker)](./removemarker%28_%29.md)
  Removes `aMarker` from the receiver, without consulting the client view for approval.
- [func trackMarker(NSRulerMarker, withMouseEvent: NSEvent) -> Bool](./trackmarker%28_,withmouseevent%29.md)
  Tracks the mouse to add `aMarker` based on the initial mouse-down or mouse-dragged event `theEvent`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/markers)*