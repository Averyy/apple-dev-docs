# init(coder:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an item from data in an unarchiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: An unarchiver object.

## See Also

### Creating items
- [convenience init(title: String?, image: UIImage?, primaryAction: UIAction?, menu: UIMenu?)](./init%28title,image,primaryaction,menu%29.md)
  Creates a plain-style item using the specified title, image, primary action, and context menu.
- [convenience init(title: String?, image: UIImage?, target: AnyObject?, action: Selector?, menu: UIMenu?)](./init%28title,image,target,action,menu%29.md)
  Creates a plain-style item using the specified title, image, target, action, and context menu.
- [init()](./init%28%29.md)
  Initializes the item to its default state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(coder:))*