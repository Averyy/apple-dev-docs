# supportedModes

**Framework**: App Intents  
**Kind**: property  
**Role**: Type Property

The supported modes for running the app intent.

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

## Discussion

Use this property to specify whether your app needs to be in the foreground or background when running your app intent’s action. You can assign one or more values to this property:

- The [`background`](../intentmodes/background.md) option runs the action entirely in the background.
- The [`immediate`](../intentmodes/foregroundmode/immediate.md) foreground mode brings the app to the foreground before the action runs.
- The [`dynamic`](../intentmodes/foregroundmode/dynamic.md) foreground mode runs the app in the background and optionally transitions it to the foreground.
- The [`deferred`](../intentmodes/foregroundmode/deferred.md) foreground mode runs the app in the background, but transitions it to the foreground before the action completes.
- The [`foreground`](../intentmodes/foreground.md) and [`background`](../intentmodes/background.md) options run the app in the foreground whenever possible, but allow it to run in the background as needed.
- The [`background`](../intentmodes/background.md) and [`dynamic`](../intentmodes/foregroundmode/dynamic.md) foreground modes run the app in either the foreground or background, but prefer the background.
- The [`background`](../intentmodes/background.md) and [`deferred`](../intentmodes/foregroundmode/deferred.md) foreground modes start the action in the background and transition to the foreground before the action finishes.

The following example shows how to specify the [`background`](../intentmodes/background.md) and [`deferred`](../intentmodes/foregroundmode/deferred.md) foreground modes for this property:

```swift
struct SomeIntent: AppIntent {
    static let supportedModes: IntentModes = [.background, .foreground(.deferred)]

    ...
}
```

In your app intent’s [`perform()`](./perform%28%29.md) method, consult the information in the [`systemContext`](./systemcontext.md) property of your app intent to determine whether your app is currently in the foreground or background.  The [`currentMode`](../intentsystemcontext/currentmode.md) property of [`IntentSystemContext`](../intentsystemcontext.md) contains the current runtime mode. You can also use the [`canContinueInForeground`](../intentmodes/current/cancontinueinforeground.md) property of the current mode to determine if a transition to the foreground is available. For more information, see [`IntentModes.Current`](../intentmodes/current.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/supportedmodes-5zhmb)*