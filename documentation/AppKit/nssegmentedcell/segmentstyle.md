# segmentStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The visual style used to display the segmented control.

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

This property contains an `NSSegmentStyle` value that specifies the visual display used by the control.

## See Also

### Related Documentation
- [NSSegmentedControl.Style](../nssegmentedcontrol/style.md)
  The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](../nssegmentedcontrol/segmentstyle.md).
### Specifying Segment Visual Styles
- [func interiorBackgroundStyle(forSegment: Int) -> NSView.BackgroundStyle](./interiorbackgroundstyle%28forsegment%29.md)
  Returns the interior background style for the specified segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcell/segmentstyle)*