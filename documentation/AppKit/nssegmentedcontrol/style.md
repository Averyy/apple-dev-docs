# NSSegmentedControl.Style

**Framework**: AppKit  
**Kind**: enum

The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](nssegmentedcontrol/segmentstyle.md).

**Availability**:
- macOS 10.5+

## Declaration

```swift
enum Style
```

## Topics

### Constants
- [NSSegmentedControl.Style.automatic](nssegmentedcontrol/style/automatic.md)
  The appearance of the segmented control is automatically determined based on the type of window in which the control is displayed and the position within the window.
- [NSSegmentedControl.Style.rounded](nssegmentedcontrol/style/rounded.md)
  The control is displayed using the rounded style.
- [NSSegmentedControl.Style.texturedRounded](nssegmentedcontrol/style/texturedrounded.md)
  The control is displayed using the textured rounded style. In macOS 10.7 and later, this style uses the artwork defined for [`NSSegmentedControl.Style.texturedSquare`](nssegmentedcontrol/style/texturedsquare.md), so you should specify [`NSSegmentedControl.Style.texturedSquare`](nssegmentedcontrol/style/texturedsquare.md) instead.
- [NSSegmentedControl.Style.roundRect](nssegmentedcontrol/style/roundrect.md)
  The control is displayed using the round rect style.
- [NSSegmentedControl.Style.texturedSquare](nssegmentedcontrol/style/texturedsquare.md)
  The control is displayed using the textured square style.
- [NSSegmentedControl.Style.capsule](nssegmentedcontrol/style/capsule.md)
  The control is displayed using the capsule style. In macOS 10.7 and later, this style uses the artwork defined for [`NSSegmentedControl.Style.texturedSquare`](nssegmentedcontrol/style/texturedsquare.md), so you should specify [`NSSegmentedControl.Style.texturedSquare`](nssegmentedcontrol/style/texturedsquare.md) instead.
- [NSSegmentedControl.Style.smallSquare](nssegmentedcontrol/style/smallsquare.md)
  The control is displayed using the small square style.
- [NSSegmentedControl.Style.separated](nssegmentedcontrol/style/separated.md)
  The segments in the control are displayed very close to each other but not touching. For example, Safari in macOS 10.10 and later uses this style for the previous and next page segmented control.
### Initializers
- [init?(rawValue: Int)](nssegmentedcontrol/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var trackingMode: NSSegmentedControl.SwitchTracking](nssegmentedcontrol/trackingmode.md)
  The type of tracking behavior the control exhibits.
- [NSSegmentedControl.SwitchTracking](nssegmentedcontrol/switchtracking.md)
  The following constants specify the type of tracking behavior a segmented control exhibits. They are used by [`trackingMode`](nssegmentedcontrol/trackingmode.md).
- [var segmentStyle: NSSegmentedControl.Style](nssegmentedcontrol/segmentstyle.md)
  The visual style used to display the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/style)*