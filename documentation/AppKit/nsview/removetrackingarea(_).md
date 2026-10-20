# removeTrackingArea(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes a given tracking area from the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func removeTrackingArea(_ trackingArea: NSTrackingArea)
```

```objc
- (void) removeTrackingArea:(NSTrackingArea *) trackingArea;
```

## Parameters

- `trackingArea`: The tracking area to remove from the view.

## See Also

### Managing Tracking Areas
- [func addTrackingArea(NSTrackingArea)](./addtrackingarea%28_%29.md)
  Adds a given tracking area to the view.
- [var trackingAreas: [NSTrackingArea]](./trackingareas.md)
  An array of the view’s tracking areas.
- [func updateTrackingAreas()](./updatetrackingareas%28%29.md)
  Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](./didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removetrackingarea(_:))*