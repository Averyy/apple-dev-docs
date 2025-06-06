# adjustsImageWhenAncestorFocused

**Framework**: UIKit  
**Kind**: property

Allows [`UIImageView`](uiimageview.md) to respond when an ancestor becomes focused.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
@MainActor
var adjustsImageWhenAncestorFocused: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true) and an ancestor of the image view becomes focused, the image view adjusts the frame of its image using the [`focusedFrameGuide`](uiimageview/focusedframeguide.md) property. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var focusedFrameGuide: UILayoutGuide](uiimageview/focusedframeguide.md)
  The layout guide to use when the image view is focused.
- [var masksFocusEffectToContents: Bool](uiimageview/masksfocuseffecttocontents.md)
  A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/adjustsimagewhenancestorfocused)*