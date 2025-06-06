# action

**Framework**: UIKit  
**Kind**: property

The selector defining the action message to send to the target object when the user taps this bar button item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var action: Selector? { get set }
```

#### Discussion

If the value of this property is `nil`, no action message is sent. The default value is `nil`.

## See Also

- [var primaryAction: UIAction?](uibarbuttonitem/primaryaction.md)
  The action associated with the item.
- [var changesSelectionAsPrimaryAction: Bool](uibarbuttonitem/changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button represents an action or selection.
- [var target: AnyObject?](uibarbuttonitem/target.md)
  The object that receives an action when the user selects the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/action)*