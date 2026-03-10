# IntentSystemContext

**Framework**: App Intents  
**Kind**: struct

Information that the system makes available to an app intent while it performs its action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct IntentSystemContext
```

#### Overview

Access information the system provides to your app intent while it performs its action in its [`perform()`](appintent/perform().md) implementation. The provided information can vary and include information for each platform. For example, in watchOS, the intent system context includes a precise timestamp when a person started the app intent’s action using the Action button on Apple Watch Ultra.

## Topics

### Instance Properties
- [var currentMode: IntentModes.Current](intentsystemcontext/currentmode.md)
  A value that indicates the foreground and background behavior for app intent’s action.
- [var preciseTimestamp: Date?](intentsystemcontext/precisetimestamp.md)
  A precise timestamp for the performed action.

## See Also

- [struct IntentDeprecation](intentdeprecation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentsystemcontext)*