# deferred

**Framework**: App Intents  
**Kind**: property

The system brings the app to the foreground while it performs the intent’s action or just before returning from its perform function.

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
static var deferred: IntentModes.ForegroundMode { get }
```

#### Discussion

When you choose the `.deferred` foreground mode, explicitly bring your app to the foreground as part of your [`perform()`](appintent/perform().md) implementation or let the system bring it to the foreground before it returns the result of your `perform()` implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/foregroundmode/deferred)*