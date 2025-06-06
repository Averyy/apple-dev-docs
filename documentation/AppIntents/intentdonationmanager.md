# IntentDonationManager

**Framework**: App Intents  
**Kind**: struct

A type you use to donate intents to the system, or delete intents when they become irrelevant.

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
struct IntentDonationManager
```

## Topics

### Getting the donation manager
- [static var shared: IntentDonationManager](intentdonationmanager/shared.md)
### Deleting previous donations
- [func deleteDonations(matching: IntentDonationMatchingPredicate) async throws -> [IntentDonationIdentifier]](intentdonationmanager/deletedonations(matching:).md)
  Deletes all transcript records matching the given predicate and returns their identifiers.
### Instance Methods
- [func donate(intent: some AppIntent) -> IntentDonationIdentifier](intentdonationmanager/donate(intent:)-57fg4.md)
  Donates an AppIntent to the transcript.
- [func donate(intent: some AppIntent) async throws -> IntentDonationIdentifier](intentdonationmanager/donate(intent:)-hly2.md)
  Donates an AppIntent to the transcript.
- [func donate(intent: some AppIntent, result: some IntentResult) async throws -> IntentDonationIdentifier](intentdonationmanager/donate(intent:result:)-1ltmi.md)
  Donates an AppIntent and IntentResult to the transcript.
- [func donate(intent: some AppIntent, result: some IntentResult) -> IntentDonationIdentifier](intentdonationmanager/donate(intent:result:)-7ztce.md)
  Donates an AppIntent and IntentResult to the transcript.

## See Also

- [struct IntentDonationIdentifier](intentdonationidentifier.md)
  An opaque type that identifies a specific donation to the system.
- [struct IntentDonationMatchingPredicate](intentdonationmatchingpredicate.md)
  The match conditions that identify a set of previously donated app intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmanager)*