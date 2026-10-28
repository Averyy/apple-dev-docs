# state

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current state of the interaction object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var state: UIBandSelectionInteraction.State { get }
```

```objc
@property (nonatomic, readonly) UIBandSelectionInteractionState state;
```

## Discussion

Use the current state to determine what actions to take in your handler. For example, when an interaction object is in the selecting state, you might highlight items in your view that are inside the current selection rectangle.

## See Also

### Getting the interaction state
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that specifies whether the object is ready to detect interactions.
- [var initialModifierFlags: UIKeyModifierFlags](./initialmodifierflags.md)
  The pressed modifier keys at the start of the interaction.
- [UIBandSelectionInteraction.State](./state-swift.enum.md)
  Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.property)*