# imageLayoutGuide

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A guide for positioning the image in the content view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var imageLayoutGuide: UILayoutGuide? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UILayoutGuide * imageLayoutGuide;
```

## Discussion

If the configuration doesn’t specify an image, the value of this property is `nil`.

If you apply a new configuration without secondary text to the content view, the system removes this layout guide from the view and deactivates any constraints associated with it.

## See Also

### Managing the content layout
- [var textLayoutGuide: UILayoutGuide?](./textlayoutguide.md)
  A guide for positioning the primary text in the content view.
- [var secondaryTextLayoutGuide: UILayoutGuide?](./secondarytextlayoutguide.md)
  A guide for positioning the secondary text in the content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentview/imagelayoutguide)*