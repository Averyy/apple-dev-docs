# backgroundColor

**Framework**: UIKit  
**Kind**: property

The background color of the action button.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var backgroundColor: UIColor! { get set }
```

#### Discussion

The default value of this property is determined by the value of the [`style`](uicontextualaction/style-swift.property.md) property, which determines the default appearance of the button. Assigning a new color to this property changes the background to the color that you specify.

## See Also

- [var title: String?](uicontextualaction/title.md)
  The title displayed on the action button.
- [var image: UIImage?](uicontextualaction/image.md)
  The image to display in the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextualaction/backgroundcolor)*