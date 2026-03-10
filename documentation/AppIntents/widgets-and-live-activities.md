# Widgets, Live Activities, and controls

**Framework**: App Intents

Use app intents make your widgets and Live Activities interactive, offer controls, and suggest widgets in Smart Stacks.

#### Overview

App Intents allows you to bring additional functionality to widgets and Live Activites, and are key to offering controls. While widgets offer personalization and glanceable information, Live Activities display up-to-date information, and controls allow people to perform actions in Control Center, on the Lock Screen, or from the Action button. Each feature uses [`WidgetKit`](https://developer.apple.com/documentation/WidgetKit), and Live Activities additionally use [`ActivityKit`](https://developer.apple.com/documentation/ActivityKit). With App Intents, you can:

- Provide hints to the system so it can automatically suggest widgets in Smart Stacks.
- Add interactive buttons or toggles to widgets and Live Activities.
- Create interactive controls that people place in Control Center, on the Lock Screen, or on the Action button.

## Topics

### Essentials
- [Adding interactivity to widgets and Live Activities](../WidgetKit/Adding-interactivity-to-widgets-and-Live-Activities.md)
  Include buttons or toggles in a widget or Live Activity to offer app functionality without launching the app.
- [Developing a WidgetKit strategy](../WidgetKit/Developing-a-WidgetKit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
### Controls
- [Controls](../WidgetKit/Controls-Collection.md)
  Offer controls that people place in Control Center, on the Lock Screen, and on the Action button to quickly perform an action from your app.
- [protocol ControlConfigurationIntent](controlconfigurationintent.md)
  An interface for configuring a Control Center module.
### Live Activities
- [Live Activities](../WidgetKit/LiveActivities-Collection.md)
  Let people track updates from your app with Live Activities.
- [protocol LiveActivityStartingIntent](liveactivitystartingintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity.
- [protocol LiveActivityIntent](liveactivityintent.md)
  An intent that starts, pauses, or otherwise modifies a Live Activity when it runs.
- [ActivityKit](../ActivityKit/ActivityKit.md)
  Share live updates from your app as Live Activities on iPhone, iPad, Apple Watch, and the Mac.
### Widgets
- [Increasing the visibility of widgets in Smart Stacks](../WidgetKit/Widget-Suggestions-In-Smart-Stacks.md)
  Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [Migrating widgets from SiriKit Intents to App Intents](../WidgetKit/Migrating-from-SiriKit-Intents-to-App-Intents.md)
  Configure your widgets for backward compatibility.
- [protocol WidgetConfigurationIntent](widgetconfigurationintent.md)
  An interface for configuring a WidgetKit widget.
- [WidgetKit](../WidgetKit/WidgetKit.md)
  Extend the reach of your app by creating widgets, watch complications, Live Activities, and controls.

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
- [Action button on iPhone and Apple Watch](actionbutton.md)
  Enable people to run your App Shortcuts with the Action button on iPhone or to start your app’s workout or dive sessions using the Action button on Apple Watch.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/widgets-and-live-activities)*