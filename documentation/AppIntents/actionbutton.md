# Action button on iPhone and Apple Watch

**Framework**: App Intents

Enable people to run your App Shortcuts with the Action button on iPhone or to start your app’s workout or dive sessions using the Action button on Apple Watch.

#### Overview

On supported iPhone models, people can choose a single App Shortcut to perform an app’s action when they press the Action button by selecting an App Shortcut in Settings > Action button. To give users quick access to your app’s functionality, create App Shortcuts for your high-value app intents using the [`init(intent:phrases:shortTitle:systemImageName:)`](appshortcut/init(intent:phrases:shorttitle:systemimagename:)-8yntq.md) or [`init(intent:phrases:shortTitle:systemImageName:parameterPresentation:)`](appshortcut/init(intent:phrases:shorttitle:systemimagename:parameterpresentation:).md) initializer. For additional information, see [`App Shortcuts`](app-shortcuts.md).

On supported Apple Watch models, people can choose to start workout or dive session using the Action button in Settings > Action Button. To add your app to the list of available workout or dive apps, implement an App Intent that adopts the [`StartWorkoutIntent`](startworkoutintent.md) or [`StartDiveIntent`](startdiveintent.md) protocol. For more information, see [`Responding to the Action button on Apple Watch Ultra`](actionbuttonarticle.md).

For design guidance, see [`Human Interface Guidelines > App Shortcuts`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/app-shortcuts) and [`Human Interface Guidelines > Action button`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/action-button).

## Topics

### Responding to the Action button
- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
  Use App Intents to register actions for your app.
- [protocol StartWorkoutIntent](startworkoutintent.md)
  An App Intent for starting a workout.
- [protocol PauseWorkoutIntent](pauseworkoutintent.md)
  An App Intent that lets someone pause your app’s current workout session.
- [protocol ResumeWorkoutIntent](resumeworkoutintent.md)
  An App Intent that lets someone resume your app’s paused workout session.
- [protocol StartDiveIntent](startdiveintent.md)
  An App Intent that lets people start a dive session when they press the Action button on Apple Watch Ultra.
- [struct ConfirmationActionName](confirmationactionname.md)

## See Also

- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.
- [Developing a WidgetKit strategy](../WidgetKit/Developing-a-WidgetKit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, watch complications, and Live Activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/actionbutton)*