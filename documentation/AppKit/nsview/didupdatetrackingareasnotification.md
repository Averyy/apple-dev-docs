# didUpdateTrackingAreasNotification

**Framework**: AppKit  
**Kind**: property

Posted whenever a view recalculates its tracking areas.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class let didUpdateTrackingAreasNotification: NSNotification.Name
```

#### Discussion

It is sent after the view receives [`updateTrackingAreas()`](nsview/updatetrackingareas().md).

## See Also

- [func addTrackingArea(NSTrackingArea)](nsview/addtrackingarea(_:).md)
  Adds a given tracking area to the view.
- [func removeTrackingArea(NSTrackingArea)](nsview/removetrackingarea(_:).md)
  Removes a given tracking area from the view.
- [var trackingAreas: [NSTrackingArea]](nsview/trackingareas.md)
  An array of the view’s tracking areas.
- [func updateTrackingAreas()](nsview/updatetrackingareas.md)
  Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/didupdatetrackingareasnotification)*