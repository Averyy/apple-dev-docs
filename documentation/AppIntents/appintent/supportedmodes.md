# supportedModes

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The foreground and background modes the app intent supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var supportedModes: IntentModes { get }
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)
- [Getting started with the App Intents framework](getting-started-with-the-app-intents-framework.md)

#### Discussion

Use this property to specify whether your app needs to be in the foreground or background when running an app intent’s action. You can assign one or more values to this property:

- Specify [`background`](intentmodes/background.md) to run the action entirely in the background.
- Specify the [`immediate`](intentmodes/foregroundmode/immediate.md) foreground mode to bring the app to the foreground before the action runs.
- Specify the [`dynamic`](intentmodes/foregroundmode/dynamic.md) foreground mode to run the app in the background and optionally transition it to the foreground.
- Specify the [`deferred`](intentmodes/foregroundmode/deferred.md) foreground mode to run the app in the background, and then transition it to the foreground before the action completes.
- Combine the [`foreground`](intentmodes/foreground.md) and [`background`](intentmodes/background.md) options to run the app in the foreground whenever possible, but allow it to run in the background as needed.
- Combine the [`background`](intentmodes/background.md) and [`dynamic`](intentmodes/foregroundmode/dynamic.md) foreground mode to run the app in either the foreground or background, but to prefer the background.
- Combine the [`background`](intentmodes/background.md) and [`deferred`](intentmodes/foregroundmode/deferred.md) foreground mode to start the action in the background and transition to the foreground before the action finishes.

The following example shows how to specify the [`background`](intentmodes/background.md) and [`deferred`](intentmodes/foregroundmode/deferred.md) foreground modes for this property:

```swift
struct SomeIntent: AppIntent {
    static let supportedModes: IntentModes = [.background, .foreground(.deferred)]

    ...
}
```

In your app intent’s [`perform()`](appintent/perform().md) method, consult the information in the [`systemContext`](appintent/systemcontext.md) property of your app intent to determine whether your code is currently running in the foreground or background.  The [`currentMode`](intentsystemcontext/currentmode.md) property of [`IntentSystemContext`](intentsystemcontext.md) contains the current mode. You can also use the [`canContinueInForeground`](intentmodes/current/cancontinueinforeground.md) property to determine if a transition to the foreground is possible. For more information, see [`IntentModes.Current`](intentmodes/current.md).

## See Also

- [struct IntentModes](intentmodes.md)
  A set of options you use to configure the runtime behavior of an app intent.
- [func continueInForeground(IntentDialog?, alwaysConfirm: Bool) async throws](appintent/continueinforeground(_:alwaysconfirm:).md)
  Attempts to transition the app to the foreground after optionally requesting permission to do so.
- [func needsToContinueInForegroundError(IntentDialog?, alwaysConfirm: Bool) -> AppIntentError](appintent/needstocontinueinforegrounderror(_:alwaysconfirm:).md)
  Asks the person to continue the intent’s action in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/supportedmodes)*