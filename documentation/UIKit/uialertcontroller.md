# UIAlertController

**Framework**: UIKit  
**Kind**: class

An object that displays an alert message.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAlertController
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Overview

Use this class to configure alerts and action sheets with the message that you want to display and the actions from which to choose. After configuring the alert controller with the actions and style you want, present it using the [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md) method. UIKit displays alerts and action sheets modally over your app’s content.

In addition to displaying a message to a user, you can associate actions with your alert controller to give people a way to respond. For each action you add using the [`addAction(_:)`](uialertcontroller/addaction(_:).md) method, the alert controller configures a button with the action details. When a person taps that action, the alert controller executes the block you provided when creating the action object. The following code shows how to configure an alert with a single action.

When configuring an alert with the [`UIAlertController.Style.alert`](uialertcontroller/style/alert.md) style, you can also add text fields to the alert interface. The alert controller lets you provide a block for configuring your text fields prior to display. The alert controller maintains a reference to each text field so that you can access its value later.

> ❗ **Important**:  The [`UIAlertController`](uialertcontroller.md) class is intended to be used as-is and doesn’t support subclassing. The view hierarchy for this class is private and must not be modified.

## Topics

### Creating an alert controller
- [convenience init(title: String?, message: String?, preferredStyle: UIAlertController.Style)](uialertcontroller/init(title:message:preferredstyle:).md)
  Creates and returns a view controller for displaying an alert.
### Configuring the alert
- [var title: String?](uialertcontroller/title.md)
  The title of the alert.
- [var message: String?](uialertcontroller/message.md)
  Descriptive text that provides more details about the reason for the alert.
- [var preferredStyle: UIAlertController.Style](uialertcontroller/preferredstyle.md)
  The style of the alert controller.
- [UIAlertController.Style](uialertcontroller/style.md)
  Constants indicating the type of alert to display.
### Configuring the user actions
- [func addAction(UIAlertAction)](uialertcontroller/addaction(_:).md)
  Attaches an action object to the alert or action sheet.
- [var actions: [UIAlertAction]](uialertcontroller/actions.md)
  The actions that the user can take in response to the alert or action sheet.
- [var preferredAction: UIAlertAction?](uialertcontroller/preferredaction.md)
  The preferred action for the user to take from an alert.
### Configuring text fields
- [func addTextField(configurationHandler: ((UITextField) -> Void)?)](uialertcontroller/addtextfield(configurationhandler:).md)
  Adds a text field to an alert.
- [var textFields: [UITextField]?](uialertcontroller/textfields.md)
  The array of text fields displayed by the alert.
### Configuring alert severity
- [var severity: UIAlertControllerSeverity](uialertcontroller/severity.md)
  Indicates the severity of the alert.
- [enum UIAlertControllerSeverity](uialertcontrollerseverity.md)
  Constants for specifying the severity of an alert in apps built with Mac Catalyst.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md)
  Present important information to a person or prompt them about an important choice.
- [class UIAlertAction](uialertaction.md)
  An action that can be taken when the user taps a button in an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller)*