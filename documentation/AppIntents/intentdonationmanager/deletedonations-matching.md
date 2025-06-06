# deleteDonations(matching:)

**Framework**: App Intents  
**Kind**: method

Deletes all transcript records matching the given predicate and returns their identifiers.

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
@discardableResult
func deleteDonations(matching predicate: IntentDonationMatchingPredicate) async throws -> [IntentDonationIdentifier]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmanager/deletedonations(matching:))*