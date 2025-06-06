# dismissMenu()

**Framework**: UIKit  
**Kind**: method

Dismiss the edit menu if present.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dismissMenu()
```

#### Discussion

You use this method to dismiss the menu, for example, from an observer callback in your app.

## See Also

- [var delegate: (any UIEditMenuInteractionDelegate)?](uieditmenuinteraction/delegate.md)
  An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [func presentEditMenu(with: UIEditMenuConfiguration)](uieditmenuinteraction/presenteditmenu(with:).md)
  Presents an edit menu using the object you provide for configuration.
- [func reloadVisibleMenu()](uieditmenuinteraction/reloadvisiblemenu.md)
  Updates the actions an edit menu displays.
- [func updateVisibleMenuPosition(animated: Bool)](uieditmenuinteraction/updatevisiblemenuposition(animated:).md)
  Updates the position of the currently visible menu with an option to animate the action.
- [func location(in: UIView?) -> CGPoint](uieditmenuinteraction/location(in:).md)
  Returns the location of the user interaction in the specified view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/dismissmenu())*