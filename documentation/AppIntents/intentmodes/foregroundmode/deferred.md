# deferred

**Framework**: App Intents  
**Kind**: property

An option to bring the app to the foreground while running the intent’s action or shortly before the action completes.

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
static var deferred: IntentModes.ForegroundMode { get }
```

#### Discussion

This option ensures the transition of the app to the foreground. Call the `AppIntent/continueInForeground(_:alwaysConfirm:) ` or [`needsToContinueInForegroundError(_:alwaysConfirm:)`](appintent/needstocontinueinforegrounderror(_:alwaysconfirm:).md) method from your intent’s [`perform()`](appintent/perform().md) method to transition to the foreground at the time you choose. If you don’t call one of these methods, the system transitions the app to the foreground at the end of your [`perform()`](appintent/perform().md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/foregroundmode/deferred)*