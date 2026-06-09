# deleteDonations(matching:)

**Framework**: App Intents  
**Kind**: method

Deletes the donations that match the criteria in the specified predicate.

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
@discardableResult
func deleteDonations(matching predicate: IntentDonationMatchingPredicate) async throws -> [IntentDonationIdentifier]
```

#### Return Value

An array with the donation identifiers for each deleted donation.

#### Discussion

Delete donations as part of your app’s overall cleanup and maintenance tasks. You might delete a donation when the data required to perform the action isn’t available. For example, if someone deletes app-specific data with an associated entity, delete all of the donations that contain the entity in a required parameter. You might also delete a donation if someone undoes the associated action, or if the actions are no longer relevant.

## Parameters

- `predicate`: A predicate that identifies the donations to delete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmanager/deletedonations(matching:))*