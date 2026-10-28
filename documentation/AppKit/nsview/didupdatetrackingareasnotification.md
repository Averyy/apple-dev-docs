# didUpdateTrackingAreasNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted whenever a view recalculates its tracking areas.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class let didUpdateTrackingAreasNotification: NSNotification.Name
```

```c
extern NSNotificationName NSViewDidUpdateTrackingAreasNotification;
```

## Discussion

It is sent after the view receives [`updateTrackingAreas()`](./updatetrackingareas%28%29.md).

## See Also

### Managing Tracking Areas
- [func addTrackingArea(NSTrackingArea)](./addtrackingarea%28_%29.md)
  Adds a given tracking area to the view.
- [func removeTrackingArea(NSTrackingArea)](./removetrackingarea%28_%29.md)
  Removes a given tracking area from the view.
- [var trackingAreas: [NSTrackingArea]](./trackingareas.md)
  An array of the view’s tracking areas.
- [func updateTrackingAreas()](./updatetrackingareas%28%29.md)
  Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/didupdatetrackingareasnotification)*