# Hardware interactions

**Framework**: App Intents

Run your App Shortcuts from the Action button on iPhone or Apple Watch, or launch your own conversational app from the side button on iPhone.

#### Overview

On supported iPhone models, people can run custom actions quickly using the Action button. This button is configurable in Settings, so people can assign any App Shortcuts you create to quickly access your app’s features. In select regions, people can also place custom actions on the side button of an iPhone to launch your conversational app.

On supported Apple Watch models, people can start a workout or dive session using the device’s Action button. This button is also configurable in Settings, and supports app intents that support the [`StartWorkoutIntent`](startworkoutintent.md) or [`StartDiveIntent`](startdiveintent.md) protocol.

For more information about how to create App Shortcuts, see [`App Shortcuts`](app-shortcuts.md). For design guidance related to the Action button, see [`Action button`](https://developer.apple.com/design/Human-Interface-Guidelines/action-button).

## Topics

### Action button
- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
  Use App Intents to register actions for your app.
- [struct ConfirmationActionName](confirmationactionname.md)
### Dive support
- [protocol StartDiveIntent](startdiveintent.md)
  An App Intent that lets people start a dive session when they press the Action button on Apple Watch Ultra.
### Workout support
- [protocol StartWorkoutIntent](startworkoutintent.md)
  An App Intent for starting a workout.
- [protocol PauseWorkoutIntent](pauseworkoutintent.md)
  An App Intent that lets someone pause your app’s current workout session.
- [protocol ResumeWorkoutIntent](resumeworkoutintent.md)
  An App Intent that lets someone resume your app’s paused workout session.
### Side button
- [Launching your voice-based conversational app from the side button of iPhone](launching-your-voice-based-conversational-app-from-the-side-button-of-iphone.md)
  Let people in Japan configure the side button of iPhone to launch your voice-based conversational app.

## See Also

- [Adopting App Intents to support system experiences](adopting-app-intents-to-support-system-experiences.md)
  Create app intents and entities so people can use your app’s content and actions across system experiences.
- [Apple Intelligence and Siri AI](apple-intelligence-and-siri-ai.md)
  Integrate your app with Apple Intelligence and bring it to Siri AI.
- [Spotlight integration](spotlight.md)
  Add your entities to your app’s Spotlight index, and automate the indexing of your content.
- [App Shortcuts](app-shortcuts.md)
  Improve the experience of using your app intents and entities in system experiences like Siri, Spotlight, and the Shortcuts app.
- [Widgets, Live Activities, and Controls](widgets-live-activities-and-controls.md)
  Implement interactive widgets, controls, watch complications, and Live Activities using app intents.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.
- [Visual intelligence](visual-intelligence.md)
  Match images to your app’s content and report the results to the Visual Intelligence framework using an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/hardware-interactions)*