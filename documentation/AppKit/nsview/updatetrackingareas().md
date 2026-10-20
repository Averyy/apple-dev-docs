# updateTrackingAreas()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked automatically when the view’s geometry changes such that its tracking areas need to be recalculated.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func updateTrackingAreas()
```

```objc
- (void) updateTrackingAreas;
```

#### Discussion

You should override this method to remove out of date tracking areas and add recomputed tracking areas; your implementation should call `super`.

## See Also

### Managing Tracking Areas
- [func addTrackingArea(NSTrackingArea)](./addtrackingarea%28_%29.md)
  Adds a given tracking area to the view.
- [func removeTrackingArea(NSTrackingArea)](./removetrackingarea%28_%29.md)
  Removes a given tracking area from the view.
- [var trackingAreas: [NSTrackingArea]](./trackingareas.md)
  An array of the view’s tracking areas.
- [class let didUpdateTrackingAreasNotification: NSNotification.Name](./didupdatetrackingareasnotification.md)
  Posted whenever a view recalculates its tracking areas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/updatetrackingareas())*