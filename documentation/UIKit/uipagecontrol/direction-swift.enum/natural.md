# UIPageControl.Direction.natural

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A direction that infers the lay out from the system’s locale.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case natural
```

```c
UIPageControlDirectionNatural
```

#### Discussion

Use this case to lay out the page control’s indicators in the natural direction of the system’s locale. By default, this means [`UIPageControl.Direction.leftToRight`](./lefttoright.md) for left-to-right languages and [`UIPageControl.Direction.rightToLeft`](./righttoleft.md) for right-to-left languages.

## See Also

### Directions
- [UIPageControl.Direction.leftToRight](./lefttoright.md)
  A direction that lays out the page indicators from left to right.
- [UIPageControl.Direction.rightToLeft](./righttoleft.md)
  A direction that lays out the page indicators from right to left.
- [UIPageControl.Direction.topToBottom](./toptobottom.md)
  A direction that lays out the page indicators from top to bottom.
- [UIPageControl.Direction.bottomToTop](./bottomtotop.md)
  A direction that lays out the page indicators from bottom to top.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/direction-swift.enum/natural)*