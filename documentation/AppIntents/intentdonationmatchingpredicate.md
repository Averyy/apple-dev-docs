# IntentDonationMatchingPredicate

**Framework**: App Intents  
**Kind**: struct

The match conditions that identify a set of previously donated app intents.

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
struct IntentDonationMatchingPredicate
```

## Topics

### Creating a predicate
- [static func donationIdentifier(IntentDonationIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/donationidentifier(_:).md)
  Delete the transcript record with the given donation identifier
- [static func entityIdentifier(EntityIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/entityidentifier(_:).md)
  Delete all transcript records referencing the given AppEntity instance
- [static func intentType(any AppIntent.Type, entityIdentifier: EntityIdentifier?) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/intenttype(_:entityidentifier:).md)
  Delete all transcript records for the given AppIntent type, optionally only those referencing a given AppEntity instance identifier

## See Also

- [struct IntentDonationManager](intentdonationmanager.md)
  A type you use to donate intents to the system, or delete intents when they become irrelevant.
- [struct IntentDonationIdentifier](intentdonationidentifier.md)
  An opaque type that identifies a specific donation to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmatchingpredicate)*