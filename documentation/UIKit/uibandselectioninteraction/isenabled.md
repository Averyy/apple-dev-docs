# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that specifies whether the object is ready to detect interactions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the [`UIBandSelectionInteraction`](uibandselectioninteraction.md) object is ready to detect pointer-based events in its owning view and initiate interactions. If the value is [`false`](https://developer.apple.com/documentation/swift/false), the object ignores events and doesn’t start interactions. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var initialModifierFlags: UIKeyModifierFlags](uibandselectioninteraction/initialmodifierflags.md)
  The pressed modifier keys at the start of the interaction.
- [var state: UIBandSelectionInteraction.State](uibandselectioninteraction/state-swift.property.md)
  The current state of the interaction object.
- [UIBandSelectionInteraction.State](uibandselectioninteraction/state-swift.enum.md)
  Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/isenabled)*