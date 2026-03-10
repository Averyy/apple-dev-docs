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

- [Adopting App Intents to support system experiences](adopting-app-intents-to-support-system-experiences.md)
  Create app intents and entities to incorporate system experiences such as Spotlight, visual intelligence, and Shortcuts.
- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
  Annotate your app entity types to support Spotlight indexing, and donate entities to make them findable in searches.
- [Launching your voice-based conversational app from the side button of iPhone](launching-your-voice-based-conversational-app-from-the-side-button-of-iphone.md)
  Let people in Japan configure the side button of iPhone to launch your voice-based conversational app.
- [Siri](siri.md)
  Let people complete tasks with voice commands, search, and other system experiences by integrating your app with Siri and Apple Intelligence.
- [Visual intelligence](visual-intelligence.md)
  Integrate your app with visual intelligence and include your content in its search results.
- [App Shortcuts](app-shortcuts.md)
  Integrate your app’s intents and entities with the Shortcuts app, Siri, Spotlight, and the Action button on supported iPhone and Apple Watch models.
- [Widgets, Live Activities, and controls](widgets-and-live-activities.md)
  Use app intents make your widgets and Live Activities interactive, offer controls, and suggest widgets in Smart Stacks.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/actionbutton)*