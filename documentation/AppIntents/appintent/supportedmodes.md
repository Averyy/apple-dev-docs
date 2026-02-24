# supportedModes

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

Defines the supported modes that describe the behavior of your app intent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var supportedModes: IntentModes { get }
```

#### Discussion

The suppprted modes determine whether the intent performs its action in the background, the foreground, or a combination of both. Available modes include:

- **`.background`**: The intent performs entirely in the background without foregrounding the app. This mode results in the same behavior as setting [`openAppWhenRun`](appintent/openappwhenrun.md) to `false`.
- **`.foreground(.immediate)`**: The intent foregrounds the app immediately after parameter resolution and before [`perform()`](appintent/perform().md) runs. This mode results in the same behavior as setting [`openAppWhenRun`](appintent/openappwhenrun.md) to `true`.
- **`.foreground(.dynamic)`**: The app intent to can foreground the app during execution based on runtime conditions. This mode is results in the same behavior as creating an app intent that conforms to [`ForegroundContinuableIntent`](foregroundcontinuableintent.md).
- **`.foreground(.deferred)`**: Enables the app to perform in the background initially, with the guarantee that the app will be foregrounded either by you within [`perform()`](appintent/perform().md) or by the system before returning from [`perform()`](appintent/perform().md).

Additionally, you can set `supportedModes` to a combination of background and foreground modes:

- **`[.background, .foreground]` or `[.background, .foreground(.immediate)]`**: Allows the app intent to perform its action in the foreground per default and to perform it in the background as a fallback when it can’t run in the foreground.
- **`[.background, .foreground(.dynamic)]`**: The app intent can perform its action with the app in the foreground or in the background, defaulting to running it with the app in the background. In your [`perform()`](appintent/perform().md) implementation, you can request to open your app in the foreground with the system determining whether or not it can grant the request.
- **`[.background, .foreground(.deferred)]`**: The app intent can perform its action with the app in the background and the foreground execution. Per default, the system runs the action in the background and the system guarantees to bring your app to the foreground when you request it in your [`perform()`](appintent/perform().md) implementation or automatically before it returns the result of the `perform()` method.

When handling both background and foreground modes you can consult `SystemContext`’s `SystemContext/currentMode` property within your [`perform()`](appintent/perform().md) implementation to determine the active mode and decide whether foregrounding your app is appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/supportedmodes)*