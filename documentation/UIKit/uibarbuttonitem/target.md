# target

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that receives an action when the user selects the item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
weak var target: AnyObject? { get set }
```

```objc
@property (nonatomic, weak, readwrite, nullable) id target;
```

#### Discussion

If `nil`, the action message is passed up the responder chain where it may be handled by any object implementing a method corresponding to the selector held by the [`action`](./action.md) property. The default value is `nil`.

## See Also

### Managing the action
- [var primaryAction: UIAction?](./primaryaction.md)
  The action associated with the item.
- [var changesSelectionAsPrimaryAction: Bool](./changesselectionasprimaryaction.md)
  A Boolean value that indicates whether the button represents an action or selection.
- [var action: Selector?](./action.md)
  The selector defining the action message to send to the target object when the user taps this bar button item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/target)*