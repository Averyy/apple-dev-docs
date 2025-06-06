# presentEditMenu(with:)

**Framework**: UIKit  
**Kind**: method

Presents an edit menu using the object you provide for configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentEditMenu(with configuration: UIEditMenuConfiguration)
```

#### Discussion

You use this method to display the edit menu. The method calls [`editMenuInteraction(_:menuFor:suggestedActions:)`](uieditmenuinteractiondelegate/editmenuinteraction(_:menufor:suggestedactions:).md) on the interaction object’s delegate and updates the UI with the menu the delegate returns. This method dismisses any active menus before presenting the new menu.

The following example presents the menu from a gesture recognizer and provides the location of the gesture as the location for this interaction.

```swift
    @objc func didLongPress(_ recognizer: UIGestureRecognizer) {
        let location = recognizer.location(in: self.view)
        let configuration = UIEditMenuConfiguration(identifier: nil, sourcePoint: location)

        if let interaction = editMenuInteraction {
            // Presenting the edit menu interaction
            interaction.presentEditMenu(with: configuration)
        }
    }
```

## Parameters

- `configuration`: The object containing the configuration details for the menu.

## See Also

- [var delegate: (any UIEditMenuInteractionDelegate)?](uieditmenuinteraction/delegate.md)
  An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [func reloadVisibleMenu()](uieditmenuinteraction/reloadvisiblemenu.md)
  Updates the actions an edit menu displays.
- [func updateVisibleMenuPosition(animated: Bool)](uieditmenuinteraction/updatevisiblemenuposition(animated:).md)
  Updates the position of the currently visible menu with an option to animate the action.
- [func dismissMenu()](uieditmenuinteraction/dismissmenu.md)
  Dismiss the edit menu if present.
- [func location(in: UIView?) -> CGPoint](uieditmenuinteraction/location(in:).md)
  Returns the location of the user interaction in the specified view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/presenteditmenu(with:))*