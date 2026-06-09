# IntentDonationManager

**Framework**: App Intents  
**Kind**: struct

A type you use to teach the system about the actions people take using your app.

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
struct IntentDonationManager
```

## Mentions

- [Donating your app’s data and actions to the system](donating-your-apps-data-and-actions-to-the-system.md)

#### Overview

Use the shared `IntentDonationManager` instance to share your app’s actions with the system. When someone completes an interaction with your app, create a relevant app intent and donate it using this type. Over time, the system combines your donations with other information to identify patterns and predict the actions a person might take in the future. System features can then proactively suggest actions on the Lock Screen, in the Siri Suggestions widget, in Search, and in other system interfaces.

Make donations only for actions that people initiate from your app or its interface. For each donation, provide as much detail as you can about the action, and make the donation only after the person completes the action. If the action generates an interesting result, include a result value with your donation. You don’t need to donate app intents that the system creates on your behalf, because the system already donates them for you. For example, if someone uses the Shortcuts app to run one of your app intents, the system donates that app intent and any results automatically.

When a particular action is no longer relevant, delete it to improve the quality of future system suggestions. Make the removal of stale donations a routine cleanup task for your app. For example, you might remove donations when someone deletes the data associated with those donations, or if someone undoes an action shortly after performing it.

This type offers both synchronous and asynchronous methods to donate your app intents. Use the asynchronous methods when you need to know whether a donation succeeds or fails. For example, use the asynchronous methods to identify issues during testing or to ensure a donation actually succeeded in your production code. The asynchronous methods throw an error when a donation fails, while the synchronous methods fail quietly.

## Topics

### Getting the donation manager
- [static let shared: IntentDonationManager](intentdonationmanager/shared.md)
  The shared instance of this class.
### Donating intents to the system
- [func donate(intent: some AppIntent) -> IntentDonationIdentifier](intentdonationmanager/donate(intent:)-57fg4.md)
  Donates the specified app intent to the system synchronously.
- [func donate(intent: some AppIntent) async throws -> IntentDonationIdentifier](intentdonationmanager/donate(intent:)-hly2.md)
  Donates the specified app intent to the system asynchronously.
- [func donate(intent: some AppIntent, result: some IntentResult) async throws -> IntentDonationIdentifier](intentdonationmanager/donate(intent:result:)-1ltmi.md)
  Donates the specified app intent and result to the system asynchronously.
- [func donate(intent: some AppIntent, result: some IntentResult) -> IntentDonationIdentifier](intentdonationmanager/donate(intent:result:)-7ztce.md)
  Donates the specified app intent and result to the system synchronously.
### Deleting previous donations
- [func deleteDonations(matching: IntentDonationMatchingPredicate) async throws -> [IntentDonationIdentifier]](intentdonationmanager/deletedonations(matching:).md)
  Deletes the donations that match the criteria in the specified predicate.

## See Also

- [struct IntentDonationIdentifier](intentdonationidentifier.md)
  An opaque type that identifies a specific donation to the system.
- [struct IntentDonationMatchingPredicate](intentdonationmatchingpredicate.md)
  A type you use to specify previously donated app intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmanager)*