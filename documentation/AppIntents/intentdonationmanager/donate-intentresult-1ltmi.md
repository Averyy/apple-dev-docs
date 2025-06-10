# donate(intent:result:)

**Framework**: App Intents  
**Kind**: method

Donates an AppIntent and IntentResult to the transcript.

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
@discardableResult
func donate(intent: some AppIntent, result: some IntentResult) async throws -> IntentDonationIdentifier
```

## See Also

- [func donate(intent: some AppIntent) -> IntentDonationIdentifier](intentdonationmanager/donate(intent:)-57fg4.md)
  Donates an AppIntent to the transcript.
- [func donate(intent: some AppIntent) async throws -> IntentDonationIdentifier](intentdonationmanager/donate(intent:)-hly2.md)
  Donates an AppIntent to the transcript.
- [func donate(intent: some AppIntent, result: some IntentResult) -> IntentDonationIdentifier](intentdonationmanager/donate(intent:result:)-7ztce.md)
  Donates an AppIntent and IntentResult to the transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmanager/donate(intent:result:)-1ltmi)*