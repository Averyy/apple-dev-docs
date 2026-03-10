# Focus

**Framework**: App Intents

Adjust your app’s behavior and filter incoming notifications when the current Focus changes.

#### Overview

![None](https://docs-assets.developer.apple.com/published/5df0da09dac6ff6a8d59c38d2909275b/focus-filters-hero%402x.png)

People use Focus on macOS, iOS, and iPadOS to minimize distractions. For example, someone might use a Work Focus to hide notifications from personal email or message accounts. When someone engages a Focus, the system executes your app’s custom [`SetFocusFilterIntent`](setfocusfilterintent.md). Define a version of this intent to update your app’s configuration and filter incoming notifications.

> **Note**:  Session 10121: [`Meet Focus filters`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10121).

## Topics

### Focus filters
- [protocol SetFocusFilterIntent](setfocusfilterintent.md)
  An interface for providing an app intent that you use to adapt your app’s behavior when Focus changes.
- [Defining your app’s Focus filter](defining-your-app-s-focus-filter.md)
  Customize your app’s behavior to reflect the device’s current Focus.
- [struct FocusFilterAppContext](focusfilterappcontext.md)
  A type that contains app-specific contextual information for a particular Focus, such as the notification filter criteria to apply.
- [struct FocusFilterSuggestionContext](focusfiltersuggestioncontext.md)
  A type you use to suggest app configurations for a given Focus.
### Errors
- [enum SetFocusFilterIntentError](setfocusfilterintenterror.md)
  Errors that can occur when you try to retrieve the current Focus configuration settings.

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
- [Action button on iPhone and Apple Watch](actionbutton.md)
  Enable people to run your App Shortcuts with the Action button on iPhone or to start your app’s workout or dive sessions using the Action button on Apple Watch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/focus)*