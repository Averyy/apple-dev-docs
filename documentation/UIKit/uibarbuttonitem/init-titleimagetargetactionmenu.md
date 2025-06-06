# init(title:image:target:action:menu:)

**Framework**: UIKit  
**Kind**: init

Creates a plain-style item using the specified title, image, target, action, and context menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(title: String?, image: UIImage?, target: AnyObject?, action: Selector?, menu: UIMenu? = nil)
```

#### Return Value

A newly initialized [`UIBarButtonItem`](uibarbuttonitem.md).

## Parameters

- `title`: The item’s title. If  , a title doesn’t appear.
- `image`: The images displayed on the bar derive from this image. If this image is too large to fit on the bar, it’s scaled to fit. Typically, the size of a toolbar and navigation bar image is   x   points. The system uses the alpha values in the source image to create the images, ignoring opaque values.
- `target`: The object that receives the   message.
- `action`: The action to send to   when a person selects this item.
- `menu`: The menu to present. The context menu displays in response to a person tapping the item.

## See Also

- [convenience init(title: String?, image: UIImage?, primaryAction: UIAction?, menu: UIMenu?)](uibarbuttonitem/init(title:image:primaryaction:menu:).md)
  Creates a plain-style item using the specified title, image, primary action, and context menu.
- [init()](uibarbuttonitem/init.md)
  Initializes the item to its default state.
- [init?(coder: NSCoder)](uibarbuttonitem/init(coder:).md)
  Creates an item from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(title:image:target:action:menu:))*