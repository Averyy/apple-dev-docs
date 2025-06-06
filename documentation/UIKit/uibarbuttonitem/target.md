# target

**Framework**: UIKit  
**Kind**: property

The object that receives an action when the user selects the item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var target: AnyObject? { get set }
```

#### Discussion

If `nil`, the action message is passed up the responder chain where it may be handled by any object implementing a method corresponding to the selector held by the [`action`](uibarbuttonitem/action.md) property. The default value is `nil`.

## See Also

- [var primaryAction: UIAction?](uibarbuttonitem/primaryaction.md)
  The action associated with the item.
- [var changesSelectionAsPrimaryAction: Bool](uibarbuttonitem/changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button represents an action or selection.
- [var action: Selector?](uibarbuttonitem/action.md)
  The selector defining the action message to send to the target object when the user taps this bar button item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/target)*