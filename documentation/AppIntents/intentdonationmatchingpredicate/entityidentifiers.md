# entityIdentifiers(_:)

**Framework**: App Intents  
**Kind**: method

Creates a predicate that matches donations that refer to one of the specified entities.

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
static func entityIdentifiers(_ identifiers: [EntityIdentifier]) -> IntentDonationMatchingPredicate
```

#### Return Value

A predicate that matches a donation if it contains at least one of the specified entities.

#### Discussion

When you delete the data for multiple entities from your app’s data store, use this method to remove donations that refer to one of those [`AppEntity`](appentity.md) instances. This predicate matches all donations in which the app intent contains a parameter with one of the specified entities. Removing those donations prevents the system from suggesting an app intent that your app can’t run because it doesn’t have the needed data.

## Parameters

- `identifiers`: An array of identifiers for your app’s entities. Typically, you find an entity’s identifier in its `id` property, which you add as part of your implementation of the [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmatchingpredicate/entityidentifiers(_:))*