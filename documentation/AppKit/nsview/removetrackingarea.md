# removeTrackingArea(_:)

**Framework**: AppKit  
**Kind**: method

Removes a given tracking area from the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func removeTrackingArea(_ trackingArea: NSTrackingArea)
```

## Parameters

- `trackingArea`: The tracking area to remove from the view.

## See Also

- [func addTrackingArea(NSTrackingArea)](nsview/addtrackingarea(_:).md)
  Adds a given tracking area to the view.
- [var trackingAreas: [NSTrackingArea]](nsview/trackingareas.md)
  An array of the view’s tracking areas.
- [func updateTrackingAreas()](nsview/updatetrackingareas.md)
  Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](nsview/didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removetrackingarea(_:))*