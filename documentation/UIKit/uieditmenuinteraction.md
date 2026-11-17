# UIEditMenuInteraction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIEditMenuInteraction : NSObject
```

## Mentions

- [Building a desktop-class iPad app](./building-a-desktop-class-ipad-app.md)

## Overview

Edit menu interactions provide actions, such as cut, copy, and paste, for the content a view displays. The interaction chooses its presentation style based on the input method. For touch interactions, the system presents the actions in an edit menu that displays a compact, horizontal list. For a secondary click on devices with pointer-based input, the system presents them in a context menu.

Standard UIKit classes, such as [`UITextView`](./uitextview.md) and [`UITextField`](./uitextfield.md), are preconfigured to use edit menu interactions.

To add an edit menu interaction to a generic view, create the interaction and pass an optional delegate to the default initializer, add it to your view with [`addInteraction(_:)`](./uiview/addinteraction%28_%29.md), and add a gesture recognizer whose action calls [`presentEditMenu(with:)`](./uieditmenuinteraction/presenteditmenu%28with%29.md). The following example presents the menu when a long press begins.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // Add the edit menu interaction.
    let interaction = UIEditMenuInteraction(delegate: self)
    editMenuInteraction = interaction
    interactionView.addInteraction(interaction)

    // Create the gesture recognizer.
    let longPress = UILongPressGestureRecognizer(target: self, action: #selector(didLongPress(_:)))
    longPress.allowedTouchTypes = [UITouch.TouchType.direct.rawValue as NSNumber]
    interactionView.addGestureRecognizer(longPress)
}

@objc func didLongPress(_ recognizer: UIGestureRecognizer) {
    // Present the menu once, when the long press begins.
    guard recognizer.state == .began else { return }

    // Use the coordinate space of the view that has the interaction.
    let location = recognizer.location(in: interactionView)
    let configuration = UIEditMenuConfiguration(identifier: nil, sourcePoint: location)

    // Present the edit menu interaction.
    editMenuInteraction?.presentEditMenu(with: configuration)
}
```

Gesture recognizers support touch input like the long-press gesture in the example above. When someone performs a secondary click on a device with pointer-based input, the interaction presents the menu automatically.

By default, an edit menu interaction generates a menu that includes commands for the standard edit actions your view implements. For details about these actions, see [`UIResponderStandardEditActions`](./uiresponderstandardeditactions.md). Use the methods in the [`UIEditMenuInteractionDelegate`](./uieditmenuinteractiondelegate.md) protocol to add items to the menu and to set the rectangle the menu points to. For text views, specify the items the menu displays for specific text ranges by using methods from the [`UITextViewDelegate`](./uitextviewdelegate.md), [`UITextFieldDelegate`](./uitextfielddelegate.md), or [`UITextInput`](./uitextinput.md) protocols.

## Share code with Mac Catalyst

In iOS and iPadOS, an edit menu interaction can present a menu in two ways. Calling [`presentEditMenu(with:)`](./uieditmenuinteraction/presenteditmenu%28with%29.md) presents an edit menu, and a secondary click presents a context menu. Mac Catalyst doesn’t have the edit menu presentation, so [`presentEditMenu(with:)`](./uieditmenuinteraction/presenteditmenu%28with%29.md) has no effect there, and a secondary click is the only way to present a menu.

Because the interaction asks the same delegate method for the menu, keep the [`presentEditMenu(with:)`](./uieditmenuinteraction/presenteditmenu%28with%29.md) call in shared code and implement [`editMenuInteraction(_:menuFor:suggestedActions:)`](./uieditmenuinteractiondelegate/editmenuinteraction%28_,menufor,suggestedactions%29.md) once.

> **Related Sessions from WWDC22**:  Session 10071: [Adopt desktop-class editing interactions](https://developer.apple.com/wwdc22/10071)

## Topics

### Creating an edit menu interaction
- [init(delegate: (any UIEditMenuInteractionDelegate)?)](./uieditmenuinteraction/init%28delegate%29.md)
  Initializes an edit menu interaction object with the delegate object you specify.
### Responding to menu requests
- [var delegate: (any UIEditMenuInteractionDelegate)?](./uieditmenuinteraction/delegate.md)
  An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [protocol UIEditMenuInteractionDelegate](./uieditmenuinteractiondelegate.md)
  The methods for customizing the menu the interaction displays.
### Managing edit menu interactions
- [func presentEditMenu(with: UIEditMenuConfiguration)](./uieditmenuinteraction/presenteditmenu%28with%29.md)
  Presents an edit menu using the object you provide for configuration.
- [func reloadVisibleMenu()](./uieditmenuinteraction/reloadvisiblemenu%28%29.md)
  Updates the actions an edit menu displays.
- [func updateVisibleMenuPosition(animated: Bool)](./uieditmenuinteraction/updatevisiblemenuposition%28animated%29.md)
  Updates the position of the currently visible menu with an option to animate the action.
- [func dismissMenu()](./uieditmenuinteraction/dismissmenu%28%29.md)
  Dismiss the edit menu if present.
- [func location(in: UIView?) -> CGPoint](./uieditmenuinteraction/location%28in%29.md)
  Returns the location of the user interaction in the specified view’s coordinate system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UIInteraction](./uiinteraction.md)

## See Also

### Related Documentation
- [Building a desktop-class iPad app](./building-a-desktop-class-ipad-app.md)
  Optimize your iPad app’s user experience by adopting desktop-class enhancements for multitasking with Stage Manager, document interactions, text editing, search, and more.
### Edit menus
- [protocol UIEditMenuInteractionDelegate](./uieditmenuinteractiondelegate.md)
  The methods for customizing the menu the interaction displays.
- [class UIEditMenuConfiguration](./uieditmenuconfiguration.md)
  An object containing the configuration details for the menu your app presents in response to an edit menu interaction.
- [protocol UIResponderStandardEditActions](./uiresponderstandardeditactions.md)
  A set of standard methods that apps can adopt to support editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uieditmenuinteraction)*