# state

**Framework**: UIKit  
**Kind**: property

The current state of the interaction object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var state: UIBandSelectionInteraction.State { get }
```

#### Discussion

Use the current state to determine what actions to take in your handler. For example, when an interaction object is in the selecting state, you might highlight items in your view that are inside the current selection rectangle.

## See Also

- [var isEnabled: Bool](uibandselectioninteraction/isenabled.md)
  A Boolean value that specifies whether the object is ready to detect interactions.
- [var initialModifierFlags: UIKeyModifierFlags](uibandselectioninteraction/initialmodifierflags.md)
  The pressed modifier keys at the start of the interaction.
- [UIBandSelectionInteraction.State](uibandselectioninteraction/state-swift.enum.md)
  Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/state-swift.property)*