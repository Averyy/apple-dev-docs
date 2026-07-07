# canContinueInForeground

**Framework**: App Intents  
**Kind**: property

A Boolean value that indicates whether running the app intent in the foreground is possible.

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
var canContinueInForeground: Bool { get }
```

#### Discussion

Check the value of this property to determine if running the app intent in the foreground is supported in the current context. Typically, you check this value if your app intent supports both foreground and background runtime modes, and need to switch from background to foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/current/cancontinueinforeground)*