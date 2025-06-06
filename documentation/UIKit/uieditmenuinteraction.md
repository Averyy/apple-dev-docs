# UIEditMenuInteraction

**Framework**: Uikit  
**Kind**: class

An interaction that provides edit operations using a menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIEditMenuInteraction
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Overview

Edit menu interactions provide edit actions — such as cut, copy, and paste — for the content a view displays. The presentation style the interaction uses to display the actions conforms to the input method of the interaction. For touch interactions, the actions display in an editing menu. When responding to a secondary click on devices with pointer-based input, the actions display in a context menu.

Standard UIKit classes, such as [`UITextView`](uitextview.md) and [`UITextField`](uitextfield.md), are preconfigured to use edit menu interactions.

To add an edit menu interaction to a generic view:

1. Create an edit menu interaction object, and pass an optional delegate into the default initializer.
2. Call the [`addInteraction(_:)`](uiview/addinteraction(_:).md) method on your view to add the interaction.
3. Create a gesture recognizer to trigger the interaction and add it to the view.

The following example creates an edit menu interaction triggered by a long press.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // Add the edit menu interaction.
    editMenuInteraction = UIEditMenuInteraction(delegate: self)
    interactionView.addInteraction(editMenuInteraction!)

    // Create the gesture recognizer.
    let longPress = UILongPressGestureRecognizer(target: self, action: #selector(didLongPress(_:)))
    longPress.allowedTouchTypes = [UITouch.TouchType.direct.rawValue as NSNumber]
    interactionView.addGestureRecognizer(longPress)
}

@objc func didLongPress(_ recognizer: UIGestureRecognizer) {
    let location = recognizer.location(in: self.view)
    let configuration = UIEditMenuConfiguration(identifier: nil, sourcePoint: location)

    if let interaction = editMenuInteraction {
        // Present the edit menu interaction.
        interaction.presentEditMenu(with: configuration)
    }
}
```

By default, an edit menu interaction generates a menu that includes commands for the standard edit actions your view implements. For more information on these actions, see [`UIResponderStandardEditActions`](uiresponderstandardeditactions.md). You can use the interaction’s delegate to add additional items to the menu and set the target rectangle to display around using methods in the [`UIEditMenuInteractionDelegate`](uieditmenuinteractiondelegate.md) protocol. For text views, you can specify the items the menu displays for specific text ranges using methods from the [`UITextViewDelegate`](uitextviewdelegate.md), [`UITextFieldDelegate`](uitextfielddelegate.md), or [`UITextInput`](uitextinput.md) protocols.

> **Note**:  Session 10071: [`Adopt desktop-class editing interactions`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10071)

## Topics

### Creating an edit menu interaction
- [init(delegate: (any UIEditMenuInteractionDelegate)?)](uieditmenuinteraction/init(delegate:).md)
  Initializes an edit menu interaction object with the delegate object you specify.
### Managing edit menu interactions
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
- [func location(in: UIView?) -> CGPoint](uieditmenuinteraction/location(in:).md)
  Returns the location of the user interaction in the specified view’s coordinate system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)
  Optimize your iPad app’s user experience by adopting desktop-class enhancements for multitasking with Stage Manager, document interactions, text editing, search, and more.
- [protocol UIEditMenuInteractionDelegate](uieditmenuinteractiondelegate.md)
  The methods for customizing the menu the interaction displays.
- [class UIEditMenuConfiguration](uieditmenuconfiguration.md)
  An object containing the configuration details for the menu your app presents in response to an edit menu interaction.
- [protocol UIResponderStandardEditActions](uiresponderstandardeditactions.md)
  A set of standard methods that apps can adopt to support editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/uieditmenuinteraction)*