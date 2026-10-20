# reloadVisibleMenu()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the actions an edit menu displays.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func reloadVisibleMenu()
```

```objc
- (void) reloadVisibleMenu;
```

#### Discussion

You use this method to update the actions the menu displays. The method calls [`editMenuInteraction(_:menuFor:suggestedActions:)`](../uieditmenuinteractiondelegate/editmenuinteraction%28_,menufor,suggestedactions%29.md) and updates the UI with the menu the delegate returns. The method has no effect if no menu is present.

## See Also

### Managing edit menu interactions
- [var delegate: (any UIEditMenuInteractionDelegate)?](./delegate.md)
  An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [func presentEditMenu(with: UIEditMenuConfiguration)](./presenteditmenu%28with%29.md)
  Presents an edit menu using the object you provide for configuration.
- [func updateVisibleMenuPosition(animated: Bool)](./updatevisiblemenuposition%28animated%29.md)
  Updates the position of the currently visible menu with an option to animate the action.
- [func dismissMenu()](./dismissmenu%28%29.md)
  Dismiss the edit menu if present.
- [func location(in: UIView?) -> CGPoint](./location%28in%29.md)
  Returns the location of the user interaction in the specified view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/reloadvisiblemenu())*