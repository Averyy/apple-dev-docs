# trackingAreas

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of the view’s tracking areas.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var trackingAreas: [NSTrackingArea] { get }
```

```objc
@property (copy, readonly) NSArray<NSTrackingArea *> * trackingAreas;
```

#### Discussion

This property contains an array of [`NSTrackingArea`](../nstrackingarea.md) objects. If the view has no tracking areas, the array is empty.

## See Also

### Managing Tracking Areas
- [func addTrackingArea(NSTrackingArea)](./addtrackingarea%28_%29.md)
  Adds a given tracking area to the view.
- [func removeTrackingArea(NSTrackingArea)](./removetrackingarea%28_%29.md)
  Removes a given tracking area from the view.
- [func updateTrackingAreas()](./updatetrackingareas%28%29.md)
  Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](./didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/trackingareas)*