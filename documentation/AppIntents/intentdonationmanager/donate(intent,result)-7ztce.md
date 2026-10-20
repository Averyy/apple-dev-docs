# donate(intent:result:)

**Framework**: App Intents  
**Kind**: method

Donates the specified app intent and result to the system synchronously.

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
func donate(intent: some AppIntent, result: some IntentResult) -> IntentDonationIdentifier
```

#### Return Value

A unique identifier you can use to refer to the donation later. The method returns this value whether the donation succeeds or fails.

#### Discussion

When someone completes an action in your app, call this method to donate a matching app intent and result. The system doesn’t run the app intent you provide, but uses the information to predict future actions. If an error occurs during the donation process, this method ignores the error.

## Parameters

- `intent`: An app intent for an action your app performed. Put enough information into the app intent that your app can replicate the action later.
- `result`: A significant result to the action. For example, specify a result that triggers a follow-up app intent.

## See Also

- [func donate(intent: some AppIntent) -> IntentDonationIdentifier](intentdonationmanager/donate(intent:)-57fg4.md)
  Donates the specified app intent to the system synchronously.
- [func donate(intent: some AppIntent) async throws -> IntentDonationIdentifier](intentdonationmanager/donate(intent:)-hly2.md)
  Donates the specified app intent to the system asynchronously.
- [func donate(intent: some AppIntent, result: some IntentResult) async throws -> IntentDonationIdentifier](intentdonationmanager/donate(intent:result:)-1ltmi.md)
  Donates the specified app intent and result to the system asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdonationmanager/donate(intent:result:)-7ztce)*