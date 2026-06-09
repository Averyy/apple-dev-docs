# IntentDonationMatchingPredicate

**Framework**: App Intents  
**Kind**: struct

A type you use to specify previously donated app intents.

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
struct IntentDonationMatchingPredicate
```

#### Overview

An `IntentDonationMatchingPredicate` matches one or more app intent donations you made previously. Use this type to specify the donations you plan to delete using the [`deleteDonations(matching:)`](intentdonationmanager/deletedonations(matching:).md) method of [`IntentDonationManager`](intentdonationmanager.md). You can create predicates to match donations with specific identifiers, or to match donations that contain specific app intents or entities. For example, if someone deletes data in your app, you can create a predicate to remove donations that refer to that data.

## Topics

### Creating a predicate
- [static func donationIdentifier(IntentDonationIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/donationidentifier(_:).md)
  Creates a predicate that matches a single, previous donation.
- [static func entityIdentifier(EntityIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/entityidentifier(_:).md)
  Creates a predicate to match any donation that contains the specified entity in a parameter.
- [static func intentType(any AppIntent.Type, entityIdentifier: EntityIdentifier?) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/intenttype(_:entityidentifier:).md)
  Creates a predicate to match app intents of the specified type that optionally refers to a specific entity.
### Type Methods
- [static func donationIdentifiers([IntentDonationIdentifier]) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/donationidentifiers(_:).md)
  Creates a predicate that matches one or more previous donations.
- [static func entityIdentifiers([EntityIdentifier]) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/entityidentifiers(_:).md)
  Creates a predicate that matches donations that refer to one of the specified entities.

## See Also

- [struct IntentDonationManager](intentdonationmanager.md)
  A type you use to teach the system about the actions people take using your app.
- [struct IntentDonationIdentifier](intentdonationidentifier.md)
  An opaque type that identifies a specific donation to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmatchingpredicate)*