# presentEditMenu(with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Presents an edit menu using the object you provide for configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func presentEditMenu(with configuration: UIEditMenuConfiguration)
```

```objc
- (void) presentEditMenuWithConfiguration:(UIEditMenuConfiguration *) configuration;
```

## Discussion

You use this method to display the edit menu. The method calls [`editMenuInteraction(_:menuFor:suggestedActions:)`](../uieditmenuinteractiondelegate/editmenuinteraction%28_,menufor,suggestedactions%29.md) on the interaction object’s delegate and updates the UI with the menu the delegate returns. This method dismisses any active menus before presenting the new menu.

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

### Managing edit menu interactions
- [var delegate: (any UIEditMenuInteractionDelegate)?](./delegate.md)
  An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [func reloadVisibleMenu()](./reloadvisiblemenu%28%29.md)
  Updates the actions an edit menu displays.
- [func updateVisibleMenuPosition(animated: Bool)](./updatevisiblemenuposition%28animated%29.md)
  Updates the position of the currently visible menu with an option to animate the action.
- [func dismissMenu()](./dismissmenu%28%29.md)
  Dismiss the edit menu if present.
- [func location(in: UIView?) -> CGPoint](./location%28in%29.md)
  Returns the location of the user interaction in the specified view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/presenteditmenu(with:))*