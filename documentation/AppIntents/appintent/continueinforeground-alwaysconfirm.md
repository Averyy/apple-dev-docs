# continueInForeground(_:alwaysConfirm:)

**Framework**: App Intents  
**Kind**: method

Attempts to transition the app to the foreground after optionally requesting permission to do so.

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
func continueInForeground(_ dialog: IntentDialog? = nil, alwaysConfirm: Bool = true) async throws
```

#### Discussion

Call this method from your app intent’s [`perform()`](appintent/perform().md) method when you want to continue running your code in the foreground. Before calling this method, use the contextual information in the intent’s [`systemContext`](appintent/systemcontext.md) property to verify the app can transition to the foreground. If you call this method and it’s not possible to transition the app to the foreground, the system throws an [`notAllowed`](appintenterror/unrecoverable/notallowed.md) error.

## Parameters

- `dialog`: The localized text you want the system to display or speak to confirm the transition.
- `alwaysConfirm`: `true` to ask the person to confirm the transition. If you specify `false`, the system might not ask for confirmation if it already received a recent confirmation. It doesn’t ask for confirmation if you recently called a `requestChoice` or `requestConfirmation` method of your intent, or asked to disambiguate a value. It does ask for confirmation if your app intent conforms to the [`ProgressReportingIntent`](progressreportingintent.md) protocol but didn’t update the progress value recently.

## See Also

- [static var supportedModes: IntentModes](appintent/supportedmodes.md)
  The foreground and background modes the app intent supports.
- [struct IntentModes](intentmodes.md)
  A set of options you use to configure the runtime behavior of an app intent.
- [func needsToContinueInForegroundError(IntentDialog?, alwaysConfirm: Bool) -> AppIntentError](appintent/needstocontinueinforegrounderror(_:alwaysconfirm:).md)
  Asks the person to continue the intent’s action in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/continueinforeground(_:alwaysconfirm:))*