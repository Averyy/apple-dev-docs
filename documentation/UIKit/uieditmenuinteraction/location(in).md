# location(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the location of the user interaction in the specified view’s coordinate system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func location(in view: UIView?) -> CGPoint
```

```objc
- (CGPoint) locationInView:(UIView *) view;
```

## Return Value

The location of the interaction in the coordinate system of view.

## Parameters

- `view`: The view containing the target coordinate system. To return a point in the window’s coordinate system, specify `nil`.

## See Also

### Managing edit menu interactions
- [var delegate: (any UIEditMenuInteractionDelegate)?](./delegate.md)
  An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [func presentEditMenu(with: UIEditMenuConfiguration)](./presenteditmenu%28with%29.md)
  Presents an edit menu using the object you provide for configuration.
- [func reloadVisibleMenu()](./reloadvisiblemenu%28%29.md)
  Updates the actions an edit menu displays.
- [func updateVisibleMenuPosition(animated: Bool)](./updatevisiblemenuposition%28animated%29.md)
  Updates the position of the currently visible menu with an option to animate the action.
- [func dismissMenu()](./dismissmenu%28%29.md)
  Dismiss the edit menu if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/location(in:))*