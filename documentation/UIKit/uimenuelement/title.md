# title

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The title of the menu element.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var title: String { get }
```

```objc
@property (nonatomic, readonly) NSString * title;
```

## See Also

### Getting the element attributes
- [var subtitle: String?](./subtitle.md)
  The subtitle to display alongside the menu element’s title.
- [var highlightStateUpdateHandler: ((UIMenuElement, Bool) -> Void)?](./highlightstateupdatehandler.md)
  A closure the system calls when the element’s highlight state changes in a menu.
- [var image: UIImage?](./image.md)
  The image to display alongside the menu element’s title.
- [var preferredImageVisibility: UIMenuElement.ImageVisibility](./preferredimagevisibility.md)
  The preferred visibility of the element’s image.
- [UIMenuElement.ImageVisibility](./imagevisibility.md)
  Visibility options for a menu element’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/title)*