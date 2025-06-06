# addItem(_:)

**Framework**: UIKit  
**Kind**: method

Associates the field behavior with the specified dynamic item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addItem(_ item: any UIDynamicItem)
```

#### Discussion

Use this method to apply a field to a dynamic item in your interface. This method adds the specified dynamic item to the field behavior’s list of dynamic items.

## Parameters

- `item`: The dynamic item whose behavior you want to modify.

## See Also

- [func removeItem(any UIDynamicItem)](uifieldbehavior/removeitem(_:).md)
  Removes the field behavior from the specified dynamic item.
- [var items: [any UIDynamicItem]](uifieldbehavior/items.md)
  The dynamic items associated with the current field behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/additem(_:))*