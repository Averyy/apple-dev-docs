# initialModifierFlags

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The pressed modifier keys at the start of the interaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var initialModifierFlags: UIKeyModifierFlags { get }
```

```objc
@property (nonatomic, readonly) UIKeyModifierFlags initialModifierFlags;
```

## Discussion

When an interaction starts, the [`UIBandSelectionInteraction`](../uibandselectioninteraction.md) object places the current pressed modifier keys in this property. Use the set of modifier keys to adjust the behavior of your handler. For example, you might extend an existing selection when someone presses the Shift key.

## See Also

### Getting the interaction state
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that specifies whether the object is ready to detect interactions.
- [var state: UIBandSelectionInteraction.State](./state-swift.property.md)
  The current state of the interaction object.
- [UIBandSelectionInteraction.State](./state-swift.enum.md)
  Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction/initialmodifierflags)*