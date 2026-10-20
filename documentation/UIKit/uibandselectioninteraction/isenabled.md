# isEnabled

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the object is ready to detect interactions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isEnabled) BOOL enabled;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), the [`UIBandSelectionInteraction`](../uibandselectioninteraction.md) object is ready to detect pointer-based events in its owning view and initiate interactions. If the value is [`false`](../../Swift/false.md), the object ignores events and doesn’t start interactions. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Getting the interaction state
- [var initialModifierFlags: UIKeyModifierFlags](./initialmodifierflags.md)
  The pressed modifier keys at the start of the interaction.
- [var state: UIBandSelectionInteraction.State](./state-swift.property.md)
  The current state of the interaction object.
- [UIBandSelectionInteraction.State](./state-swift.enum.md)
  Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/isenabled)*