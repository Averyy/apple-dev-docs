# UIBarPosition.top

**Framework**: UIKit  
**Kind**: case

Specifies that the bar is at the top of its containing view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
case top
```

#### Discussion

The system uses this as a hint to draw directional decoration accordingly. For example, any shadow would be drawn below the bar.

Instances of [`UIToolbar`](uitoolbar.md) do not appear with this position on iPhone, but they can on iPad.

## See Also

- [UIBarPosition.any](uibarposition/any.md)
  Specifies that the position is unspecified.
- [UIBarPosition.bottom](uibarposition/bottom.md)
  Specifies that the bar is at the bottom of its containing view.
- [UIBarPosition.topAttached](uibarposition/topattached.md)
  Specifies that the bar is at the top of the screen, as well as its containing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarposition/top)*