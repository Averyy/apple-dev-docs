# items

**Framework**: UIKit  
**Kind**: property

The dynamic items associated with the current field behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var items: [any UIDynamicItem] { get }
```

#### Discussion

When it is enabled, the current field applies its behavior to all of the items in the array.

## See Also

- [func addItem(any UIDynamicItem)](uifieldbehavior/additem(_:).md)
  Associates the field behavior with the specified dynamic item.
- [func removeItem(any UIDynamicItem)](uifieldbehavior/removeitem(_:).md)
  Removes the field behavior from the specified dynamic item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/items)*