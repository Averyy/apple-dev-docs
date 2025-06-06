# NSStackView.Gravity

**Framework**: AppKit  
**Kind**: enum

The gravity areas available in a stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
enum Gravity
```

#### Overview

The layout of a stack view is partitioned into three distinct areas in which you can place views. These are known as . You can use these constants to configure a stack view by way of the [`insertView(_:at:in:)`](nsstackview/insertview(_:at:in:).md) and [`setViews(_:in:)`](nsstackview/setviews(_:in:).md) methods.

In a horizontally oriented stack view, the three gravity areas are [`leading`](nsstackview/gravity/leading.md), [`NSStackView.Gravity.center`](nsstackview/gravity/center.md), and [`trailing`](nsstackview/gravity/trailing.md). The ordering of these areas depends on the user interface language, unless you’ve explicitly specified the stack view’s user interface layout direction by calling the inherited [`userInterfaceLayoutDirection`](nsview/userinterfacelayoutdirection.md) method. For a [`userInterfaceLayoutDirection`](nsview/userinterfacelayoutdirection.md) property value of [`NSUserInterfaceLayoutDirection.leftToRight`](nsuserinterfacelayoutdirection/lefttoright.md), the leading gravity area is on the left.

In a vertically oriented stack view, the three gravity areas are always [`NSStackView.Gravity.top`](nsstackview/gravity/top.md), [`NSStackView.Gravity.center`](nsstackview/gravity/center.md), and [`NSStackView.Gravity.bottom`](nsstackview/gravity/bottom.md).

The center gravity area is constrained to remain geometrically centered with an Auto Layout priority of [`defaultLow`](nslayoutconstraint/priority-swift.struct/defaultlow.md). For information about geometric spacing between gravity areas, see the description of the [`spacing`](nsstackview/spacing.md) property.

## Topics

### Constants
- [NSStackView.Gravity.top](nsstackview/gravity/top.md)
  The topmost gravity area in a vertically oriented stack view.
- [static var leading: NSStackView.Gravity](nsstackview/gravity/leading.md)
  The leftmost or rightmost gravity area in a horizontally oriented stack view, based on the user interface language or the explicitly set user interface layout direction.
- [NSStackView.Gravity.center](nsstackview/gravity/center.md)
  The center gravity area, regardless of stack view layout direction or user interface language.
- [NSStackView.Gravity.bottom](nsstackview/gravity/bottom.md)
  The bottommost gravity area in a vertically oriented stack view.
- [static var trailing: NSStackView.Gravity](nsstackview/gravity/trailing.md)
  The leftmost or rightmost gravity area in a horizontally oriented stack view, based on the user interface language or the explicitly set user interface layout direction.
### Initializers
- [init?(rawValue: Int)](nsstackview/gravity/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func addView(NSView, in: NSStackView.Gravity)](nsstackview/addview(_:in:).md)
  Adds a view to the end of the stack view gravity area.
- [func insertView(NSView, at: Int, in: NSStackView.Gravity)](nsstackview/insertview(_:at:in:).md)
  Adds a view to a stack view gravity area at a specified index position.
- [func setViews([NSView], in: NSStackView.Gravity)](nsstackview/setviews(_:in:).md)
  Specifies an array of views for a specified gravity area in the stack view, replacing any previous views in that area.
- [func removeView(NSView)](nsstackview/removeview(_:).md)
  Removes a specified view from the stack view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/gravity)*