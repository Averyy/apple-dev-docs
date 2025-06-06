# initialModifierFlags

**Framework**: UIKit  
**Kind**: property

The pressed modifier keys at the start of the interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var initialModifierFlags: UIKeyModifierFlags { get }
```

#### Discussion

When an interaction starts, the [`UIBandSelectionInteraction`](uibandselectioninteraction.md) object places the current pressed modifier keys in this property. Use the set of modifier keys to adjust the behavior of your handler. For example, you might extend an existing selection when someone presses the Shift key.

## See Also

- [var isEnabled: Bool](uibandselectioninteraction/isenabled.md)
  A Boolean value that specifies whether the object is ready to detect interactions.
- [var state: UIBandSelectionInteraction.State](uibandselectioninteraction/state-swift.property.md)
  The current state of the interaction object.
- [UIBandSelectionInteraction.State](uibandselectioninteraction/state-swift.enum.md)
  Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/initialmodifierflags)*