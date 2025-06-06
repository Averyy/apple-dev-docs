# progress

**Framework**: App Intents  
**Kind**: property

An object representing the progress of the intent’s action.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var progress: Progress { get }
```

#### Discussion

You can update  the progress as your action moves forward. Note that the system receives an update of the progress.

> ⚠️ **Warning**: This progress is available only in the app intent’s [`perform()`](appintent/perform().md) method. Trying to access the progress object outside of the `perform()` method results in a crash.

This progress is available only in the app intent’s [`perform()`](appintent/perform().md) method. Trying to access the progress object outside of the `perform()` method results in a crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/progressreportingintent/progress)*