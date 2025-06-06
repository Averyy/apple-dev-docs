# donate(intent:result:)

**Framework**: App Intents  
**Kind**: method

Donates an AppIntent and IntentResult to the transcript.

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
func donate(intent: some AppIntent, result: some IntentResult) async throws -> IntentDonationIdentifier
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmanager/donate(intent:result:)-1ltmi)*