# trackingMode

**Framework**: AppKit  
**Kind**: property

The type of tracking behavior the control exhibits.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
@MainActor
var trackingMode: NSSegmentedControl.SwitchTracking { get set }
```

#### Discussion

An [`NSSegmentedControl.SwitchTracking`](nssegmentedcontrol/switchtracking.md) value specifies how the control responds when the user presses a keyboard key or clicks, force clicks (applies pressure in a pressure-sensitive system), releases pressure, and so on. For possible values see [`NSSegmentedControl.SwitchTracking`](nssegmentedcontrol/switchtracking.md).

## See Also

- [Segmented Control Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SegmentedControl/SegmentedControl.html#//apple_ref/doc/uid/10000182i)
- [var isContinuous: Bool](nscontrol/iscontinuous.md)
  A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.
- [var doubleValueForSelectedSegment: Double](nssegmentedcontrol/doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.
- [NSSegmentedControl.SwitchTracking](nssegmentedcontrol/switchtracking.md)
  The following constants specify the type of tracking behavior a segmented control exhibits. They are used by [`trackingMode`](nssegmentedcontrol/trackingmode.md).
- [var segmentStyle: NSSegmentedControl.Style](nssegmentedcontrol/segmentstyle.md)
  The visual style used to display the control.
- [NSSegmentedControl.Style](nssegmentedcontrol/style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](nssegmentedcontrol/segmentstyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/trackingmode)*