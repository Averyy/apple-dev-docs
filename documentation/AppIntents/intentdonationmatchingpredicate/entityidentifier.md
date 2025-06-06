# entityIdentifier(_:)

**Framework**: App Intents  
**Kind**: method

Delete all transcript records referencing the given AppEntity instance

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
static func entityIdentifier(_ identifier: EntityIdentifier) -> IntentDonationMatchingPredicate
```

## See Also

- [static func donationIdentifier(IntentDonationIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/donationidentifier(_:).md)
  Delete the transcript record with the given donation identifier
- [static func intentType(any AppIntent.Type, entityIdentifier: EntityIdentifier?) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/intenttype(_:entityidentifier:).md)
  Delete all transcript records for the given AppIntent type, optionally only those referencing a given AppEntity instance identifier


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmatchingpredicate/entityidentifier(_:))*