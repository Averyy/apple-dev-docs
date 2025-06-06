# donate(intent:)

**Framework**: App Intents  
**Kind**: method

Donates an AppIntent to the transcript.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@discardableResult
func donate(intent: some AppIntent) -> IntentDonationIdentifier
```

#### Discussion

This synchronous interface is available for adopting application that haven’t adopted Swift async concurrency. Any exceptions encountered in donating this intent are ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmanager/donate(intent:)-57fg4)*