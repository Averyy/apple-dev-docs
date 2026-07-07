# intentType(_:entityIdentifier:)

**Framework**: App Intents  
**Kind**: method

Creates a predicate to match app intents of the specified type that optionally refers to a specific entity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func intentType(_ intentType: any AppIntent.Type, entityIdentifier: EntityIdentifier? = nil) -> IntentDonationMatchingPredicate
```

#### Return Value

A predicate that matches a donation when app intents of the provided type contain the entity you specified.

#### Discussion

Use this method to delete all donations with a specific type of app intent. Include a value in the `entityIdentifier` parameter to limit the deletions to those that also reference a specific [`AppEntity`](appentity.md) instance. Remove donations to prevent the system from suggesting those actions in the future.

## Parameters

- `intentType`: The app intent type to match against.
- `entityIdentifier`: The identifier for one of your app’s entities. Typically, you find an entity’s identifier in its `id` property, which you add as part of your implementation of the [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocol.

## See Also

- [static func donationIdentifier(IntentDonationIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/donationidentifier(_:).md)
  Creates a predicate that matches a single, previous donation.
- [static func entityIdentifier(EntityIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/entityidentifier(_:).md)
  Creates a predicate to match any donation that contains the specified entity in a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmatchingpredicate/intenttype(_:entityidentifier:))*