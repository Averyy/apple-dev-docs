# donationIdentifier(_:)

**Framework**: App Intents  
**Kind**: method

Delete the transcript record with the given donation identifier

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
static func donationIdentifier(_ identifier: IntentDonationIdentifier) -> IntentDonationMatchingPredicate
```

## See Also

- [static func entityIdentifier(EntityIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/entityidentifier(_:).md)
  Delete all transcript records referencing the given AppEntity instance
- [static func intentType(any AppIntent.Type, entityIdentifier: EntityIdentifier?) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/intenttype(_:entityidentifier:).md)
  Delete all transcript records for the given AppIntent type, optionally only those referencing a given AppEntity instance identifier


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmatchingpredicate/donationidentifier(_:))*