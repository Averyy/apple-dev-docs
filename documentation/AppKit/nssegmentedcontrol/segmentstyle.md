# segmentStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The visual style used to display the control.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var segmentStyle: NSSegmentedControl.Style { get set }
```

```objc
@property NSSegmentStyle segmentStyle;
```

#### Discussion

An `NSSegmentStyle` value that specifies the visual display used by the control. For possible values, see [`NSSegmentedControl.Style`](./style.md).

## See Also

### Specifying the segment behavior
- [var trackingMode: NSSegmentedControl.SwitchTracking](./trackingmode.md)
  The type of tracking behavior the control exhibits.
- [NSSegmentedControl.SwitchTracking](./switchtracking.md)
  Constants that specify the type of tracking behavior a segmented control exhibits.
- [NSSegmentedControl.Style](./style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](./segmentstyle.md).
- [var role: NSSegmentedControl.Role](./role-swift.property.md)
- [NSSegmentedControl.Role](./role-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/segmentstyle)*