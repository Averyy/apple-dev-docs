# primaryAction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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
var primaryAction: UIAction? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UIAction * primaryAction;
```

## Discussion

When you assign a new value to this property, the title and image of the item update to match the primary action’s [`title`](../uiaction/title.md) and [`image`](../uiaction/image.md).

If this property has a non-`nil` value, the system ignores the item’s [`target`](./target.md) and [`action`](./action.md) properties.

## See Also

### Managing the action
- [var changesSelectionAsPrimaryAction: Bool](./changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button represents an action or selection.
- [var action: Selector?](./action.md)
  The selector defining the action message to send to the target object when the user taps this bar button item.
- [var target: AnyObject?](./target.md)
  The object that receives an action when the user selects the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/primaryaction)*