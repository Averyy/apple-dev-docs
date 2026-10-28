# trackingMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of tracking behavior the control exhibits.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
var trackingMode: NSSegmentedControl.SwitchTracking { get set }
```

```objc
@property NSSegmentSwitchTracking trackingMode;
```

## Discussion

An [`NSSegmentedControl.SwitchTracking`](./switchtracking.md) value specifies how the control responds when the user presses a keyboard key or clicks, force clicks (applies pressure in a pressure-sensitive system), releases pressure, and so on. For possible values see [`NSSegmentedControl.SwitchTracking`](./switchtracking.md).

## See Also

### Related Documentation
- [Segmented Control Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SegmentedControl/SegmentedControl.html#//apple_ref/doc/uid/10000182i)
- [var isContinuous: Bool](../nscontrol/iscontinuous.md)
  A Boolean value indicating whether the receiver’s cell sends its action message continuously to its target during mouse tracking.
- [var doubleValueForSelectedSegment: Double](./doublevalueforselectedsegment.md)
  When the tracking mode for the control is set to use a momentary accelerator, returns a value for the selected segment.
### Specifying the segment behavior
- [NSSegmentedControl.SwitchTracking](./switchtracking.md)
  Constants that specify the type of tracking behavior a segmented control exhibits.
- [var segmentStyle: NSSegmentedControl.Style](./segmentstyle.md)
  The visual style used to display the control.
- [NSSegmentedControl.Style](./style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](./segmentstyle.md).
- [var role: NSSegmentedControl.Role](./role-swift.property.md)
- [NSSegmentedControl.Role](./role-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/trackingmode)*