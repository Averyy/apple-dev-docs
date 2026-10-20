# init(title:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a navigation item with the specified title.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(title: String)
```

```objc
- (instancetype) initWithTitle:(NSString *) title;
```

#### Return Value

A new [`UINavigationItem`](../uinavigationitem.md) object initialized with the specified title.

#### Discussion

This is the designated initializer for this class.

## Parameters

- `title`: The string to set as the navigation item’s title displayed in the center of the navigation bar.

## See Also

### Related Documentation
- [var title: String?](./title.md)
  The navigation item’s title that displays in the navigation bar.
### Initializing an item
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a navigation item from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/init(title:))*