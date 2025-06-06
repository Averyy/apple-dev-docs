# location(in:)

**Framework**: UIKit  
**Kind**: method

Returns the location of the user interaction in the specified view’s coordinate system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func location(in view: UIView?) -> CGPoint
```

#### Return Value

The location of the interaction in the coordinate system of view.

## Parameters

- `view`: The view containing the target coordinate system. To return a point in the window’s coordinate system, specify  .

## See Also

- [var delegate: (any UIEditMenuInteractionDelegate)?](uieditmenuinteraction/delegate.md)
  An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [func presentEditMenu(with: UIEditMenuConfiguration)](uieditmenuinteraction/presenteditmenu(with:).md)
  Presents an edit menu using the object you provide for configuration.
- [func reloadVisibleMenu()](uieditmenuinteraction/reloadvisiblemenu.md)
  Updates the actions an edit menu displays.
- [func updateVisibleMenuPosition(animated: Bool)](uieditmenuinteraction/updatevisiblemenuposition(animated:).md)
  Updates the position of the currently visible menu with an option to animate the action.
- [func dismissMenu()](uieditmenuinteraction/dismissmenu.md)
  Dismiss the edit menu if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/location(in:))*