# intentType(_:entityIdentifier:)

**Framework**: App Intents  
**Kind**: method

Delete all transcript records for the given AppIntent type, optionally only those referencing a given AppEntity instance identifier

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
static func intentType(_ intentType: any AppIntent.Type, entityIdentifier: EntityIdentifier? = nil) -> IntentDonationMatchingPredicate
```

## See Also

- [static func donationIdentifier(IntentDonationIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/donationidentifier(_:).md)
  Delete the transcript record with the given donation identifier
- [static func entityIdentifier(EntityIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/entityidentifier(_:).md)
  Delete all transcript records referencing the given AppEntity instance


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmatchingpredicate/intenttype(_:entityidentifier:))*