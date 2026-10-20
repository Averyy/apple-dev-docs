# NSSegmentedControl.Style

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The following constants specify the visual style used to display the segmented control. They are used by [`segmentStyle`](./segmentstyle.md).

**Availability**:
- macOS 10.5+

## Declaration

```swift
enum Style
```

```c
enum NSSegmentStyle : NSInteger;
```

## Topics

### Constants
- [NSSegmentedControl.Style.automatic](./style/automatic.md)
  The appearance of the segmented control is automatically determined based on the type of window in which the control is displayed and the position within the window.
- [NSSegmentedControl.Style.rounded](./style/rounded.md)
  The control is displayed using the rounded style.
- [NSSegmentedControl.Style.texturedRounded](./style/texturedrounded.md)
  The control is displayed using the textured rounded style. In macOS 10.7 and later, this style uses the artwork defined for [`NSSegmentedControl.Style.texturedSquare`](./style/texturedsquare.md), so you should specify [`NSSegmentedControl.Style.texturedSquare`](./style/texturedsquare.md) instead.
- [NSSegmentedControl.Style.roundRect](./style/roundrect.md)
  The control is displayed using the round rect style.
- [NSSegmentedControl.Style.texturedSquare](./style/texturedsquare.md)
  The control is displayed using the textured square style.
- [NSSegmentedControl.Style.capsule](./style/capsule.md)
  The control is displayed using the capsule style. In macOS 10.7 and later, this style uses the artwork defined for [`NSSegmentedControl.Style.texturedSquare`](./style/texturedsquare.md), so you should specify [`NSSegmentedControl.Style.texturedSquare`](./style/texturedsquare.md) instead.
- [NSSegmentedControl.Style.smallSquare](./style/smallsquare.md)
  The control is displayed using the small square style.
- [NSSegmentedControl.Style.separated](./style/separated.md)
  The segments in the control are displayed very close to each other but not touching. For example, Safari in macOS 10.10 and later uses this style for the previous and next page segmented control.
### Initializers
- [init?(rawValue: Int)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the segment behavior
- [var trackingMode: NSSegmentedControl.SwitchTracking](./trackingmode.md)
  The type of tracking behavior the control exhibits.
- [NSSegmentedControl.SwitchTracking](./switchtracking.md)
  Constants that specify the type of tracking behavior a segmented control exhibits.
- [var segmentStyle: NSSegmentedControl.Style](./segmentstyle.md)
  The visual style used to display the control.
- [var role: NSSegmentedControl.Role](./role-swift.property.md)
- [NSSegmentedControl.Role](./role-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/style)*