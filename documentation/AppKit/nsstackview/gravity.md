# NSStackView.Gravity

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The gravity areas available in a stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum Gravity
```

```c
enum NSStackViewGravity : NSInteger;
```

## Overview

The layout of a stack view is partitioned into three distinct areas in which you can place views. These are known as *gravity areas*. You can use these constants to configure a stack view by way of the [`insertView(_:at:in:)`](./insertview%28_,at,in%29.md) and [`setViews(_:in:)`](./setviews%28_,in%29.md) methods.

In a horizontally oriented stack view, the three gravity areas are [`leading`](./gravity/leading.md), [`NSStackView.Gravity.center`](./gravity/center.md), and [`trailing`](./gravity/trailing.md). The ordering of these areas depends on the user interface language, unless you’ve explicitly specified the stack view’s user interface layout direction by calling the inherited [`userInterfaceLayoutDirection`](../nsview/userinterfacelayoutdirection.md) method. For a [`userInterfaceLayoutDirection`](../nsview/userinterfacelayoutdirection.md) property value of [`NSUserInterfaceLayoutDirection.leftToRight`](../nsuserinterfacelayoutdirection/lefttoright.md), the leading gravity area is on the left.

In a vertically oriented stack view, the three gravity areas are always [`NSStackView.Gravity.top`](./gravity/top.md), [`NSStackView.Gravity.center`](./gravity/center.md), and [`NSStackView.Gravity.bottom`](./gravity/bottom.md).

The center gravity area is constrained to remain geometrically centered with an Auto Layout priority of [`defaultLow`](../nslayoutconstraint/priority-swift.struct/defaultlow.md). For information about geometric spacing between gravity areas, see the description of the [`spacing`](./spacing.md) property.

## Topics

### Constants
- [NSStackView.Gravity.top](./gravity/top.md)
  The topmost gravity area in a vertically oriented stack view.
- [static var leading: NSStackView.Gravity](./gravity/leading.md)
  The leftmost or rightmost gravity area in a horizontally oriented stack view, based on the user interface language or the explicitly set user interface layout direction.
- [NSStackView.Gravity.center](./gravity/center.md)
  The center gravity area, regardless of stack view layout direction or user interface language.
- [NSStackView.Gravity.bottom](./gravity/bottom.md)
  The bottommost gravity area in a vertically oriented stack view.
- [static var trailing: NSStackView.Gravity](./gravity/trailing.md)
  The leftmost or rightmost gravity area in a horizontally oriented stack view, based on the user interface language or the explicitly set user interface layout direction.
### Initializers
- [init?(rawValue: Int)](./gravity/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Views in Gravity Areas
- [func addView(NSView, in: NSStackView.Gravity)](./addview%28_,in%29.md)
  Adds a view to the end of the stack view gravity area.
- [func insertView(NSView, at: Int, in: NSStackView.Gravity)](./insertview%28_,at,in%29.md)
  Adds a view to a stack view gravity area at a specified index position.
- [func setViews([NSView], in: NSStackView.Gravity)](./setviews%28_,in%29.md)
  Specifies an array of views for a specified gravity area in the stack view, replacing any previous views in that area.
- [func removeView(NSView)](./removeview%28_%29.md)
  Removes a specified view from the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/gravity)*