# cancel

**Framework**: App Intents  
**Kind**: property

A system-provided option that cancel the app intent.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static var cancel: IntentChoiceOption { get }
```

#### Discussion

Selecting this option causes the `requestChoice(between:dialog:)` method to throw a cancellation error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentchoiceoption/cancel)*