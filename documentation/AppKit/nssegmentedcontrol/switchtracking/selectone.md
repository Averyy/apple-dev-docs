# NSSegmentedControl.SwitchTracking.selectOne

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Only one segment in the control can be selected at a time.

**Availability**:
- macOS

## Declaration

```swift
case selectOne
```

```c
NSSegmentSwitchTrackingSelectOne
```

#### Discussion

This mode functions as a radio button and is illustrated by the view selection control in Finder, which allows you to toggle between icon view, list view, column view, and Cover Flow.

## See Also

### Constants
- [NSSegmentedControl.SwitchTracking.selectAny](./selectany.md)
  One or more segment cells in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.momentary](./momentary.md)
  A tracking mode that selects a segment when a person clicks within the bounds of the segment.
- [NSSegmentedControl.SwitchTracking.momentaryAccelerator](./momentaryaccelerator.md)
  A tracking mode that sends repeating actions as pressure changes on Force Touch systems, stopping when someone releases the segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/switchtracking/selectone)*