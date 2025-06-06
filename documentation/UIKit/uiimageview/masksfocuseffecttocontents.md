# masksFocusEffectToContents

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the floating focused appearance uses the image’s alpha channel.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
@MainActor
var masksFocusEffectToContents: Bool { get set }
```

#### Discussion

Set this property to [`false`](https://developer.apple.com/documentation/swift/false) when using multi-layer images or when using images that are completely opaque. Set this property to [`true`](https://developer.apple.com/documentation/swift/true) only when the image view contains a single-layer image with transparency. When set to [`true`](https://developer.apple.com/documentation/swift/true), the system uses the image’s alpha channel to create an appropriate floating focused appearance. For example, the system masks the shadow based on the alpha channel of the image.

The aspect ratio of the image view and its displayed image must be the same. Rendering with transparency affects performance, so enable this option only when needed.

## See Also

- [var adjustsImageWhenAncestorFocused: Bool](uiimageview/adjustsimagewhenancestorfocused.md)
  Allows [`UIImageView`](uiimageview.md) to respond when an ancestor becomes focused.
- [var focusedFrameGuide: UILayoutGuide](uiimageview/focusedframeguide.md)
  The layout guide to use when the image view is focused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimageview/masksfocuseffecttocontents)*