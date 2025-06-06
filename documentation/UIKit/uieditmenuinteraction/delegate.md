# delegate

**Framework**: UIKit  
**Kind**: property

An object that customizes presentation of the menu and actions to display for an edit menu interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any UIEditMenuInteractionDelegate)? { get }
```

## See Also

- [func presentEditMenu(with: UIEditMenuConfiguration)](uieditmenuinteraction/presenteditmenu(with:).md)
  Presents an edit menu using the object you provide for configuration.
- [func reloadVisibleMenu()](uieditmenuinteraction/reloadvisiblemenu.md)
  Updates the actions an edit menu displays.
- [func updateVisibleMenuPosition(animated: Bool)](uieditmenuinteraction/updatevisiblemenuposition(animated:).md)
  Updates the position of the currently visible menu with an option to animate the action.
- [func dismissMenu()](uieditmenuinteraction/dismissmenu.md)
  Dismiss the edit menu if present.
- [func location(in: UIView?) -> CGPoint](uieditmenuinteraction/location(in:).md)
  Returns the location of the user interaction in the specified view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/delegate)*