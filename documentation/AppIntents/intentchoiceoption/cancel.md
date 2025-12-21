# cancel

**Framework**: App Intents  
**Kind**: property

A system-provided option that cancel the app intent.

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
static var cancel: IntentChoiceOption { get }
```

#### Discussion

Selecting this option causes the `requestChoice(between:dialog:)` method to throw a cancellation error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentchoiceoption/cancel)*