# init(title:image:primaryAction:menu:)

**Framework**: UIKit  
**Kind**: init

Creates a plain-style item using the specified title, image, primary action, and context menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(title: String? = nil, image: UIImage? = nil, primaryAction: UIAction? = nil, menu: UIMenu? = nil)
```

#### Return Value

A newly initialized [`UIBarButtonItem`](uibarbuttonitem.md).

## Parameters

- `title`: The item’s title.
- `image`: The item’s image. The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is `20` x `20` points. The system uses the alpha values in the source image to create the images, ignoring opaque values.
- `primaryAction`: A [`UIAction`](uiaction.md) to associate with the item, which the item uses to configure its title and image. If you specify `primaryAction`, it takes precedence over `title` and `image`.
- `menu`: The menu to present. The context menu displays in response to a person tapping the item.

## See Also

- [convenience init(title: String?, image: UIImage?, target: AnyObject?, action: Selector?, menu: UIMenu?)](uibarbuttonitem/init(title:image:target:action:menu:).md)
  Creates a plain-style item using the specified title, image, target, action, and context menu.
- [init()](uibarbuttonitem/init.md)
  Initializes the item to its default state.
- [init?(coder: NSCoder)](uibarbuttonitem/init(coder:).md)
  Creates an item from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(title:image:primaryaction:menu:))*