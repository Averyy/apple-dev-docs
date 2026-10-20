# addTrackingArea(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a given tracking area to the view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func addTrackingArea(_ trackingArea: NSTrackingArea)
```

```objc
- (void) addTrackingArea:(NSTrackingArea *) trackingArea;
```

## Parameters

- `trackingArea`: The tracking area to add to the view.

## See Also

### Managing Tracking Areas
- [func removeTrackingArea(NSTrackingArea)](./removetrackingarea%28_%29.md)
  Removes a given tracking area from the view.
- [var trackingAreas: [NSTrackingArea]](./trackingareas.md)
  An array of the view’s tracking areas.
- [func updateTrackingAreas()](./updatetrackingareas%28%29.md)
  Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](./didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addtrackingarea(_:))*