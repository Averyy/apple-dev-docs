# trackingAreas

**Framework**: AppKit  
**Kind**: property

An array of the view’s tracking areas.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var trackingAreas: [NSTrackingArea] { get }
```

#### Discussion

This property contains an array of [`NSTrackingArea`](nstrackingarea.md) objects. If the view has no tracking areas, the array is empty.

## See Also

- [func addTrackingArea(NSTrackingArea)](nsview/addtrackingarea(_:).md)
  Adds a given tracking area to the view.
- [func removeTrackingArea(NSTrackingArea)](nsview/removetrackingarea(_:).md)
  Removes a given tracking area from the view.
- [func updateTrackingAreas()](nsview/updatetrackingareas.md)
  Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](nsview/didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/trackingareas)*