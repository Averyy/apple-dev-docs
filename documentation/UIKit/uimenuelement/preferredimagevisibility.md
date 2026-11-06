# preferredImageVisibility

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred visibility of the element’s image.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var preferredImageVisibility: UIMenuElement.ImageVisibility { get set }
```

```objc
@property (nonatomic) UIMenuElementImageVisibility preferredImageVisibility;
```

## See Also

### Getting the element attributes
- [var title: String](./title.md)
  The title of the menu element.
- [var subtitle: String?](./subtitle.md)
  The subtitle to display alongside the menu element’s title.
- [var highlightStateUpdateHandler: ((UIMenuElement, Bool) -> Void)?](./highlightstateupdatehandler.md)
  A closure the system calls when the element’s highlight state changes in a menu.
- [var image: UIImage?](./image.md)
  The image to display alongside the menu element’s title.
- [UIMenuElement.ImageVisibility](./imagevisibility.md)
  Visibility options for a menu element’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/preferredimagevisibility)*