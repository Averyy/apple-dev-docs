# changesSelectionAsPrimaryAction

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the button represents an action or selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var changesSelectionAsPrimaryAction: Bool { get set }
```

#### Discussion

When a button has this property set to [`true`](https://developer.apple.com/documentation/Swift/true), the button changes to a toggle button where tapping it changes it between selected and unselected.

## See Also

- [var primaryAction: UIAction?](uibarbuttonitem/primaryaction.md)
  The action associated with the item.
- [var action: Selector?](uibarbuttonitem/action.md)
  The selector defining the action message to send to the target object when the user taps this bar button item.
- [var target: AnyObject?](uibarbuttonitem/target.md)
  The object that receives an action when the user selects the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/changesselectionasprimaryaction)*