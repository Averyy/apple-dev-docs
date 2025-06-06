# updateTrackingAreas()

**Framework**: AppKit  
**Kind**: method

Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func updateTrackingAreas()
```

#### Discussion

You should override this method to remove out of date tracking areas and add recomputed tracking areas; your implementation should call `super`.

## See Also

- [func addTrackingArea(NSTrackingArea)](nsview/addtrackingarea(_:).md)
  Adds a given tracking area to the view.
- [func removeTrackingArea(NSTrackingArea)](nsview/removetrackingarea(_:).md)
  Removes a given tracking area from the view.
- [var trackingAreas: [NSTrackingArea]](nsview/trackingareas.md)
  An array of the view’s tracking areas.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](nsview/didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/updatetrackingareas())*