# Offering Live Activities with your App Clip

**Framework**: Appclip

Add a widget extension to your App Clip target and use ActivityKit to display Live Activities on the Lock Screen and in the Dynamic Island.

#### Overview

With Live Activities, you can display live event data on the iPhone Lock Screen and in the Dynamic Island on supported devices. Your App Clip can’t typically include app extensions, but starting with iOS 16 you can include a widget extension that offers Live Activities and displays live event data without requiring people to install your full app. For example, a sports app could display App Clip Codes at a game location to offer an App Clip to attendees of the current game. When a person launches the App Clip from the App Clip Code, the App Clip could offer a Live Activity to track a game that happens at the same time but in another city. The Live Activity enables people who watch the game in person to stay informed about another team’s game that happens in parallel.

> ❗ **Important**:  The widget extension for your App Clip can only include Live Activities. Reserve widgets that appear on the Home Screen, Lock Screen, or in Today View for your full app.

To offer a Live Activity from your App Clip:

1. Open your project in Xcode.
2. Add a widget extension target to your project and make sure to only add it to the App Clip target.
3. Make sure the widget extension only contains the Live Activity — widgets for the Home Screen, Lock Screen, or Today View aren’t available to App Clips. Remove any widget code that the Xcode template generates and only keep the Live Activity code. For example, remove the widget from the widget bundle that the template creates and only include the Live Activity in the widget bundle.
4. Add the App Clip Extension capability to your new widget extension. It adds the [`com.apple.developer.on-demand-install-capable`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.on-demand-install-capable) entitlement to the widget extension target. This capability is a requirement that allows the App Clip to include the widget extension.
5. Make sure the widget extension target uses the bundle identifier of the App Clip as a prefix to fulfill the bundle ID requirements for extensions. For example, if your App Clip has the bundle ID `com.example.exampleapp.clip`, the widget extension must use `com.example.exampleapp.clip.$thing`, where `$thing` is something like `widgetextension` or `liveactivities`.

When you’ve added the widget extension to your App Clip to offer Live Activities, add code for your Live Activity as described in [`Displaying live data with Live Activities`](https://developer.apple.com/documentation/ActivityKit/displaying-live-data-with-live-activities). For more information about Live Activities, see [`ActivityKit`](https://developer.apple.com/documentation/ActivityKit).

> **Note**:  If you already bundle a widget extension with your full app, don’t add it to the App Clip target. Instead, add a second widget extension to your project and make sure to only include it in the App Clip target. As a result, you’ll have one widget extension for your full app and one widget extension for your App Clip. Then, follow the steps above to add the App Clip Extension capability and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppClip/offering-live-activities-with-your-app-clip)*