# donate(intent:)

**Framework**: App Intents  
**Kind**: method

Donates the specified app intent to the system synchronously.

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
@discardableResult
func donate(intent: some AppIntent) -> IntentDonationIdentifier
```

#### Return Value

A unique identifier you can use to refer to the donation later. The method returns this value whether the donation succeeds or fails.

#### Discussion

When someone completes an action in your app, call this method to donate a matching app intent. The system doesn’t run the app intent you provide, but uses the information to predict future actions. If an error occurs during the donation process, this method ignores the error.

## Parameters

- `intent`: An app intent for an action the person performed. Include enough information in the app intent for you to recreate the action later.

## See Also

- [func donate(intent: some AppIntent) async throws -> IntentDonationIdentifier](intentdonationmanager/donate(intent:)-hly2.md)
  Donates the specified app intent to the system asynchronously.
- [func donate(intent: some AppIntent, result: some IntentResult) async throws -> IntentDonationIdentifier](intentdonationmanager/donate(intent:result:)-1ltmi.md)
  Donates the specified app intent and result to the system asynchronously.
- [func donate(intent: some AppIntent, result: some IntentResult) -> IntentDonationIdentifier](intentdonationmanager/donate(intent:result:)-7ztce.md)
  Donates the specified app intent and result to the system synchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmanager/donate(intent:)-57fg4)*