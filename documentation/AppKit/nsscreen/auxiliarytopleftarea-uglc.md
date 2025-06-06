# auxiliaryTopLeftArea

**Framework**: AppKit  
**Kind**: property

The unobscured portion of the top-left corner of the screen.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var auxiliaryTopLeftArea: NSRect? { get }
```

#### Discussion

If the top inset of the screen’s [`safeAreaInsets`](nsscreen/safeareainsets.md) property contains a non-zero value, the rectangle in this property is the visible top-left portion of the screen. The rectangle is specified in global screen coordinates and lies outside the safe area. If the top portion of the screen isn’t obscured, the value of this property is `nil` in Swift; in Objective-C, the value is [`NSZeroRect`](https://developer.apple.com/documentation/Foundation/NSZeroRect).

If your app offers a custom full-screen experience, use this property to determine what additional space is available for your custom content. The specified rectangle is safe to use to display your content.

## See Also

- [var visibleFrame: NSRect](nsscreen/visibleframe.md)
  The current location and dimensions of the visible screen.
- [var safeAreaInsets: NSEdgeInsets](nsscreen/safeareainsets.md)
  The distances from the screen’s edges at which content isn’t obscured.
- [var auxiliaryTopRightArea: NSRect?](nsscreen/auxiliarytoprightarea-gr2n.md)
  The unobscured portion of the top-right corner of the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/auxiliarytopleftarea-uglc)*