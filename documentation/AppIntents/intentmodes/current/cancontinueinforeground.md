# canContinueInForeground

**Framework**: App Intents  
**Kind**: property

A flag that indicates whether the app intent can continue its action while the app is in the foreground.

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
var canContinueInForeground: Bool { get }
```

#### Discussion

Check for the value of `canContinueInForeground` if your app intent supports running both in the background and foreground to determine if foregrounding is appropriate in the current context. For example, an app intent might require …. to perform its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/current/cancontinueinforeground)*