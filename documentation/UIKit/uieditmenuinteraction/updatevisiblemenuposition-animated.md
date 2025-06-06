# updateVisibleMenuPosition(animated:)

**Framework**: UIKit  
**Kind**: method

Updates the position of the currently visible menu with an option to animate the action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateVisibleMenuPosition(animated: Bool)
```

#### Discussion

You use this method to update the location of the menu. This method calls [`editMenuInteraction(_:targetRectFor:)`](uieditmenuinteractiondelegate/editmenuinteraction(_:targetrectfor:).md) and updates the position of the menu using the position the delegate returns. The method has no effect if no menu is present.

## Parameters

- `animated`:   to animate the transition to the new position;   to make the transition immediate.

## See Also

- [var delegate: (any UIEditMenuInteractionDelegate)?](uieditmenuinteraction/delegate.md)
  An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [func presentEditMenu(with: UIEditMenuConfiguration)](uieditmenuinteraction/presenteditmenu(with:).md)
  Presents an edit menu using the object you provide for configuration.
- [func reloadVisibleMenu()](uieditmenuinteraction/reloadvisiblemenu.md)
  Updates the actions an edit menu displays.
- [func dismissMenu()](uieditmenuinteraction/dismissmenu.md)
  Dismiss the edit menu if present.
- [func location(in: UIView?) -> CGPoint](uieditmenuinteraction/location(in:).md)
  Returns the location of the user interaction in the specified view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/updatevisiblemenuposition(animated:))*