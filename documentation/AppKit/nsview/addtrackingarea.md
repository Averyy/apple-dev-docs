# addTrackingArea(_:)

**Framework**: AppKit  
**Kind**: method

Adds a given tracking area to the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func addTrackingArea(_ trackingArea: NSTrackingArea)
```

## Parameters

- `trackingArea`: The tracking area to add to the view.

## See Also

- [func removeTrackingArea(NSTrackingArea)](nsview/removetrackingarea(_:).md)
  Removes a given tracking area from the view.
- [var trackingAreas: [NSTrackingArea]](nsview/trackingareas.md)
  An array of the view’s tracking areas.
- [func updateTrackingAreas()](nsview/updatetrackingareas.md)
  Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](nsview/didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addtrackingarea(_:))*