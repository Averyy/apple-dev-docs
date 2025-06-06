# primaryAction

**Framework**: UIKit  
**Kind**: property

The action associated with the item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var primaryAction: UIAction? { get set }
```

#### Discussion

When you assign a new value to this property, the title and image of the item update to match the primary action’s [`title`](uiaction/title.md) and [`image`](uiaction/image.md).

If this property has a non-`nil` value, the system ignores the item’s [`target`](uibarbuttonitem/target.md) and [`action`](uibarbuttonitem/action.md) properties.

## See Also

- [var changesSelectionAsPrimaryAction: Bool](uibarbuttonitem/changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button represents an action or selection.
- [var action: Selector?](uibarbuttonitem/action.md)
  The selector defining the action message to send to the target object when the user taps this bar button item.
- [var target: AnyObject?](uibarbuttonitem/target.md)
  The object that receives an action when the user selects the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/primaryaction)*