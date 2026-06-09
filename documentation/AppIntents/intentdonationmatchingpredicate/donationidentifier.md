# donationIdentifier(_:)

**Framework**: App Intents  
**Kind**: method

Creates a predicate that matches a single, previous donation.

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

#### Return Value

A predicate that matches the specified donation.

#### Discussion

When you donate an app intent using the methods of [`IntentDonationManager`](intentdonationmanager.md), the method returns a unique identifier for that donation. Use this method to create a predicate that matches only the donation you specified.

## Parameters

- `identifier`: A donation identifier you received after donating an app intent.

## See Also

- [static func entityIdentifier(EntityIdentifier) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/entityidentifier(_:).md)
  Creates a predicate to match any donation that contains the specified entity in a parameter.
- [static func intentType(any AppIntent.Type, entityIdentifier: EntityIdentifier?) -> IntentDonationMatchingPredicate](intentdonationmatchingpredicate/intenttype(_:entityidentifier:).md)
  Creates a predicate to match app intents of the specified type that optionally refers to a specific entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmatchingpredicate/donationidentifier(_:))*