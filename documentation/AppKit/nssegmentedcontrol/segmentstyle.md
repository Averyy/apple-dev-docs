# segmentStyle

**Framework**: AppKit  
**Kind**: property

The visual style used to display the control.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var segmentStyle: NSSegmentedControl.Style { get set }
```

#### Discussion

An `NSSegmentStyle` value that specifies the visual display used by the control. For possible values, see [`NSSegmentedControl.Style`](nssegmentedcontrol/style.md).

## See Also

- [var trackingMode: NSSegmentedControl.SwitchTracking](nssegmentedcontrol/trackingmode.md)
  The type of tracking behavior the control exhibits.
- [NSSegmentedControl.SwitchTracking](nssegmentedcontrol/switchtracking.md)
  The following constants specify the type of tracking behavior a segmented control exhibits. They are used by [`trackingMode`](nssegmentedcontrol/trackingmode.md).
- [NSSegmentedControl.Style](nssegmentedcontrol/style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](nssegmentedcontrol/segmentstyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/segmentstyle)*