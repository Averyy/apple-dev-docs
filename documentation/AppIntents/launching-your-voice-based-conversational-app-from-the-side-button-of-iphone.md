# Launching your voice-based conversational app from the side button of iPhone

**Framework**: App Intents

Let people in Japan configure the side button of iPhone to launch your voice-based conversational app.

#### Overview

By adopting the App Intents framework and offering App Shortcuts, you let people instantly access app functionality and integrate it with system experiences like Spotlight or App Shortcuts. For example, a person might place an App Shortcut you provide on the Action button. In Japan, people might place an action on the side button of iPhone that instantly launches your voice-based conversational app. People expect the voice-based conversational functionality to be instantly available when they launch your app with the side button, so make sure to let them immediately use it by starting an audio session – for example, with [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation).

> ❗ **Important**: Functionality provided by the [`activate`](assistantschemas/assistantintent/activate.md) schema API in [`App Intents`](AppIntents.md) is only available on iPhone in Japan and requires the [`Side Button Access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.side-button-access.allow) entitlement. During development, install your provisioning profile on your iPhone test device to test the functionality. For a production device, the country or region of your Apple Account must be set to Japan, and you must physically be located in Japan.

To allow people to press and hold the side button to launch your voice-based conversational app to its conversation experience:

1. Add the `com.apple.developer.side-button-access.allow` entitlement to the `.entitlements` file in your app’s Xcode project. For details on adding this entitlement, see [`Side Button Access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.side-button-access.allow).
2. Create an app intent that conforms to the [`activate`](assistantschemas/assistantintent/activate.md) app intent schema.
3. In the app intent’s [`perform()`](AppIntent/perform().md) implementation, navigate to the scene that provides voice-based conversational functionality and start an audio session.

The following example shows how an app that provides voice-based conversational functionality might implement an app intent that people in Japan can place on the side button of iPhone:

```swift
@AppIntent(schema: .assistant.activate)
struct ActivateVoiceBasedConversationSceneIntent {
    static let supportedModes: IntentModes = .foreground

    func perform() async throws -> some IntentResult {

        // Add code here to navigate to the scene in your app that provides
        // voice-based conversational functionality.
        // If applicable, pass information to your app that allows it to update
        // its data or UI in response to the invocation from
        // the side button and start voice-based conversational functionality.

        return .result()
    }
}
```

If you’re new to the AppIntents framework, refer to [`Creating your first app intent`](creating-your-first-app-intent.md) and [`Making actions and content discoverable and widely available`](making-actions-and-content-discoverable-and-widely-available.md) for additional information.

## See Also

- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
  Allow people to find your app’s content in Spotlight by donating app entities to its semantic index.
- [Focus](focus.md)
  Adjust your app’s behavior and filter incoming notifications when the current Focus changes.
- [Action button on iPhone and Apple Watch](actionbutton.md)
  Enable people to run your App Shortcuts with the Action button on iPhone or to start your app’s workout or dive sessions using the Action button on Apple Watch.
- [Developing a WidgetKit strategy](../WidgetKit/Developing-a-WidgetKit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/launching-your-voice-based-conversational-app-from-the-side-button-of-iphone)*