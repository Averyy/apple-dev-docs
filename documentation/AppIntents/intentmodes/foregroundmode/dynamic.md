# dynamic

**Framework**: App Intents  
**Kind**: property

An option to bring the app to the foreground if conditions permit it.

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
static var dynamic: IntentModes.ForegroundMode { get }
```

#### Discussion

This option allows you to choose whether to transition an action from the background to the foreground. If your app is running in the background, call the `AppIntent/continueInForeground(_:alwaysConfirm:) ` or [`needsToContinueInForegroundError(_:alwaysConfirm:)`](appintent/needstocontinueinforegrounderror(_:alwaysconfirm:).md) method from your intent’s [`perform()`](appintent/perform().md) method to bring it to the foreground. If you don’t call one of these methods, the app continues running the app intent’s code in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/foregroundmode/dynamic)*