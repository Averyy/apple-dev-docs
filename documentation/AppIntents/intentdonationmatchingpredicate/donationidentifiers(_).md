# donationIdentifiers(_:)

**Framework**: App Intents  
**Kind**: method

Creates a predicate that matches one or more previous donations.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
static func donationIdentifiers(_ identifiers: [IntentDonationIdentifier]) -> IntentDonationMatchingPredicate
```

#### Return Value

A predicate that matches the specified donations.

#### Discussion

When you donate an app intent using the methods of [`IntentDonationManager`](intentdonationmanager.md), the method returns a unique identifier for that donation. Use this method to create a predicate that matches all of the donations you specified.

## Parameters

- `identifiers`: An array of donation identifiers you received after donating app intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmatchingpredicate/donationidentifiers(_:))*