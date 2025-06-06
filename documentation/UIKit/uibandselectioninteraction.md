# UIBandSelectionInteraction

**Framework**: UIKit  
**Kind**: class

An object that tracks the selection of multiple items using pointer-based input.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIBandSelectionInteraction
```

#### Overview

Attach a [`UIBandSelectionInteraction`](uibandselectioninteraction.md) object to a custom view that contains one or more selectable items. On devices with pointer-based input, such as an iPad with a Magic Keyboard, this interaction object displays a visible selection rectangle over the view when someone clicks and drags on it. As the pointer moves, the selection rectangle expands or contracts to match. Use your interaction object’s handler to select items based on the current selection rectangle.

You create a band selection interaction object and add it to a view that contains one or more selectable items. When you create the interaction object, specify a handler to process changes to the selection rectangle. In the example, the custom view defines an `itemsInRect` method to get the items that intersect the selection rectangle. It also defines custom methods to modify the selection and commit the changes. If someone presses the Shift key at the start of the interaction, the code extends the current selection instead of replacing it.

```swift
// Create a UIBandSelectionInteraction object.
let bandSelectionInteraction = UIBandSelectionInteraction { [weak self] interaction in
    guard let strongSelf = self else { return }
    
    switch interaction.state {
    case .began:
        // Prepare the view to handle selection changes.
        strongSelf.selectionSession.begin()
    case .selecting:
        // Get the custom view items that intersect the selection rectangle.
        let newItems = strongSelf.itemsInRect(interaction.selectionRect)
        
        if interaction.initialModifierFlags == .shift {
            // If Shift is held, extend the view's current selection...
            strongSelf.selectionSession.append(newItems)
        } else {
            // ...otherwise, replace the view's selection with the new items.
            strongSelf.selectionSession.setSelection(newItems)
        }
    case .ended:
        // When the interaction ends, commit the selection changes.
        strongSelf.selectionSession.commit()
    }
}
    
// Add the interaction object to the view.
view.addInteraction(bandSelectionInteraction)
```

> **Note**:  You don’t need to add this interaction object to a collection view to handle the selection of items. [`UICollectionView`](uicollectionview.md) already supports its own multiple selection interface. For a list of methods you use to manage selections in a collection view, see [`UICollectionViewDelegate`](uicollectionviewdelegate.md).

 You don’t need to add this interaction object to a collection view to handle the selection of items. [`UICollectionView`](uicollectionview.md) already supports its own multiple selection interface. For a list of methods you use to manage selections in a collection view, see [`UICollectionViewDelegate`](uicollectionviewdelegate.md).

## Topics

### Creating a band selection interaction
- [init((UIBandSelectionInteraction) -> Void)](uibandselectioninteraction/init(_:).md)
  Creates a new band selection interaction object with the provided handler code.
### Getting the selection rectangle
- [var selectionRect: CGRect?](uibandselectioninteraction/selectionrect-2us5d.md)
  The selection rectangle for an in-progress interaction.
### Getting the interaction state
- [var isEnabled: Bool](uibandselectioninteraction/isenabled.md)
  A Boolean value that specifies whether the object is ready to detect interactions.
- [var initialModifierFlags: UIKeyModifierFlags](uibandselectioninteraction/initialmodifierflags.md)
  The pressed modifier keys at the start of the interaction.
- [var state: UIBandSelectionInteraction.State](uibandselectioninteraction/state-swift.property.md)
  The current state of the interaction object.
- [UIBandSelectionInteraction.State](uibandselectioninteraction/state-swift.enum.md)
  Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.
### Starting the interaction
- [var shouldBeginHandler: ((UIBandSelectionInteraction, CGPoint) -> Bool)?](uibandselectioninteraction/shouldbeginhandler.md)
  The handler that determines whether to start a band selection interaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [UIBandSelectionInteraction.State](uibandselectioninteraction/state-swift.enum.md)
  Constants that indicate whether a band selection interaction object is inactive or currently tracking an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibandselectioninteraction)*