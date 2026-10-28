# NSSegmentedControl.SwitchTracking.selectAny

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

One or more segment cells in the control can be selected at a time.

**Availability**:
- macOS

## Declaration

```swift
case selectAny
```

```c
NSSegmentSwitchTrackingSelectAny
```

## Discussion

This mode functions as a set of checkboxes, where any combination of segments may be on or off, and is illustrated by the font format selection control in Pages, which allows you to apply bold, italics, and underline to the selected text.

## See Also

### Constants
- [NSSegmentedControl.SwitchTracking.selectOne](./selectone.md)
  Only one segment in the control can be selected at a time.
- [NSSegmentedControl.SwitchTracking.momentary](./momentary.md)
  A tracking mode that selects a segment when a person clicks within the bounds of the segment.
- [NSSegmentedControl.SwitchTracking.momentaryAccelerator](./momentaryaccelerator.md)
  A tracking mode that sends repeating actions as pressure changes on Force Touch systems, stopping when someone releases the segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/switchtracking/selectany)*