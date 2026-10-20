# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object that customizes presentation of the menu and actions to display for an edit menu interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIEditMenuInteractionDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<UIEditMenuInteractionDelegate> delegate;
```

## See Also

### Managing edit menu interactions
- [func presentEditMenu(with: UIEditMenuConfiguration)](./presenteditmenu%28with%29.md)
  Presents an edit menu using the object you provide for configuration.
- [func reloadVisibleMenu()](./reloadvisiblemenu%28%29.md)
  Updates the actions an edit menu displays.
- [func updateVisibleMenuPosition(animated: Bool)](./updatevisiblemenuposition%28animated%29.md)
  Updates the position of the currently visible menu with an option to animate the action.
- [func dismissMenu()](./dismissmenu%28%29.md)
  Dismiss the edit menu if present.
- [func location(in: UIView?) -> CGPoint](./location%28in%29.md)
  Returns the location of the user interaction in the specified view’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction/delegate)*