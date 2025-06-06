# textLayoutGuide

**Framework**: UIKit  
**Kind**: property

A guide for positioning the primary text in the content view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textLayoutGuide: UILayoutGuide? { get }
```

#### Discussion

If the configuration doesn’t specify primary text, the value of this property is `nil`.

If you apply a new configuration without primary text to the content view, the system removes this layout guide from the view and deactivates any constraints associated with it.

## See Also

- [var secondaryTextLayoutGuide: UILayoutGuide?](uilistcontentview/secondarytextlayoutguide.md)
  A guide for positioning the secondary text in the content view.
- [var imageLayoutGuide: UILayoutGuide?](uilistcontentview/imagelayoutguide.md)
  A guide for positioning the image in the content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentview/textlayoutguide)*