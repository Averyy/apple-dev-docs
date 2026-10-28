# NSStackView.Gravity.top

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The topmost gravity area in a vertically oriented stack view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
case top
```

```c
NSStackViewGravityTop
```

## Discussion

Use only when the value of the [`orientation`](../orientation.md) property is [`NSUserInterfaceLayoutOrientation.vertical`](../../nsuserinterfacelayoutorientation/vertical.md).

## See Also

### Constants
- [static var leading: NSStackView.Gravity](./leading.md)
  The leftmost or rightmost gravity area in a horizontally oriented stack view, based on the user interface language or the explicitly set user interface layout direction.
- [NSStackView.Gravity.center](./center.md)
  The center gravity area, regardless of stack view layout direction or user interface language.
- [NSStackView.Gravity.bottom](./bottom.md)
  The bottommost gravity area in a vertically oriented stack view.
- [static var trailing: NSStackView.Gravity](./trailing.md)
  The leftmost or rightmost gravity area in a horizontally oriented stack view, based on the user interface language or the explicitly set user interface layout direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstackview/gravity/top)*