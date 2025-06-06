# segmentStyle

**Framework**: AppKit  
**Kind**: property

The visual style used to display the segmented control.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var segmentStyle: NSSegmentedControl.Style { get set }
```

#### Discussion

This property contains an `NSSegmentStyle` value that specifies the visual display used by the control.

## See Also

- [NSSegmentedControl.Style](nssegmentedcontrol/style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](nssegmentedcontrol/segmentstyle.md).
- [func interiorBackgroundStyle(forSegment: Int) -> NSView.BackgroundStyle](nssegmentedcell/interiorbackgroundstyle(forsegment:).md)
  Returns the interior background style for the specified segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/segmentstyle)*