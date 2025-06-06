# titleTextAttributes

**Framework**: UIKit  
**Kind**: property

Display attributes for the bar’s title text.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var titleTextAttributes: [NSAttributedString.Key : Any]? { get set }
```

#### Discussion

You can specify the font, text color, text shadow color, and text shadow offset for the title in the text attributes dictionary, using the text attribute keys described in [`NSAttributedString.Key`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key).

## See Also

- [var largeTitleTextAttributes: [NSAttributedString.Key : Any]?](uinavigationbar/largetitletextattributes.md)
  Display attributes for the bar’s large title text.
- [func titleVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](uinavigationbar/titleverticalpositionadjustment(for:).md)
  Returns the title’s vertical position adjustment for given bar metrics.
- [func setTitleVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](uinavigationbar/settitleverticalpositionadjustment(_:for:).md)
  Sets the title’s vertical position adjustment for given bar metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/titletextattributes)*