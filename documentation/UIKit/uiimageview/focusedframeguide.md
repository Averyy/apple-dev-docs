# focusedFrameGuide

**Framework**: UIKit  
**Kind**: property

The layout guide to use when the image view is focused.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
@MainActor
var focusedFrameGuide: UILayoutGuide { get }
```

#### Discussion

The layout guide in this property represents the display frame of the image view when it’s focused. You can use this property to align other elements of your interface to the image view or to adjust the constraints of your interface.

When the [`adjustsImageWhenAncestorFocused`](uiimageview/adjustsimagewhenancestorfocused.md) property is set to [`true`](https://developer.apple.com/documentation/Swift/true), the image view automatically applies this layout guide when the image view becomes focused.

## See Also

- [var adjustsImageWhenAncestorFocused: Bool](uiimageview/adjustsimagewhenancestorfocused.md)
  A Boolean value that determines whether the image view responds when an ancestor gains focus.
- [var masksFocusEffectToContents: Bool](uiimageview/masksfocuseffecttocontents.md)
  A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/focusedframeguide)*