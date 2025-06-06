# init(coder:)

**Framework**: UIKit  
**Kind**: init

Creates an item from data in an unarchiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init?(coder: NSCoder)
```

## Parameters

- `coder`: An unarchiver object.

## See Also

- [convenience init(title: String?, image: UIImage?, primaryAction: UIAction?, menu: UIMenu?)](uibarbuttonitem/init(title:image:primaryaction:menu:).md)
  Creates a plain-style item using the specified title, image, primary action, and context menu.
- [convenience init(title: String?, image: UIImage?, target: AnyObject?, action: Selector?, menu: UIMenu?)](uibarbuttonitem/init(title:image:target:action:menu:).md)
  Creates a plain-style item using the specified title, image, target, action, and context menu.
- [init()](uibarbuttonitem/init.md)
  Initializes the item to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(coder:))*