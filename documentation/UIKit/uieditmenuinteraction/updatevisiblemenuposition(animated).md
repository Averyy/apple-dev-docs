# updateVisibleMenuPosition(animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the position of the currently visible menu with an option to animate the action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func updateVisibleMenuPosition(animated: Bool)
```

```objc
- (void) updateVisibleMenuPositionAnimated:(BOOL) animated;
```

#### Discussion

You use this method to update the location of the menu. This method calls [`editMenuInteraction(_:targetRectFor:)`](../uieditmenuinteractiondelegate/editmenuinteraction%28_,targetrectfor%29.md) and updates the position of the menu using the position the delegate returns. The method has no effect if no menu is present.

## Parameters

- `animated`: `YES` to animate the transition to the new position; `NO` to make the transition immediate.

## See Also

### Managing edit menu interactions
- [var delegate: (any UIEditMenuInteractionDelegate)?](./delegate.md)
  An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [func presentEditMenu(with: UIEditMenuConfiguration)](./presenteditmenu%28with%29.md)
  Presents an edit menu using the object you provide for configuration.
- [func reloadVisibleMenu()](./reloadvisiblemenu%28%29.md)
  Updates the actions an edit menu displays.
- [func dismissMenu()](./dismissmenu%28%29.md)
  Dismiss the edit menu if present.
- [func location(in: UIView?) -> CGPoint](./location%28in%29.md)
  Returns the location of the user interaction in the specified view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/updatevisiblemenuposition(animated:))*