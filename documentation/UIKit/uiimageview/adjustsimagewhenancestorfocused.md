# adjustsImageWhenAncestorFocused

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the image view responds when an ancestor gains focus.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
@MainActor
var adjustsImageWhenAncestorFocused: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) and an ancestor of the image view becomes focused, the image view adjusts the frame of its image using the [`focusedFrameGuide`](uiimageview/focusedframeguide.md) property. On supported Apple TV devices, setting this property to true renders the image with a Liquid Glass effect when it gains focus.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var focusedFrameGuide: UILayoutGuide](uiimageview/focusedframeguide.md)
  The layout guide to use when the image view is focused.
- [var masksFocusEffectToContents: Bool](uiimageview/masksfocuseffecttocontents.md)
  A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/adjustsimagewhenancestorfocused)*