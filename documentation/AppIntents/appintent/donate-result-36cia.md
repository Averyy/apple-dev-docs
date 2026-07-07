# donate(result:)

**Framework**: App Intents  
**Kind**: method

Donates the app intent and a result to the system asynchronously.

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
func donate(result: some IntentResult) async throws -> IntentDonationIdentifier
```

#### Return Value

An opaque identifier you can use to manage the donation later using an [`IntentDonationManager`](intentdonationmanager.md) type.

#### Discussion

When someone interacts with your app’s interface, create an app intent for the interaction and call this method. Use this method when the result of the intent is also relevant, such as when the result of the action triggers another app intent. Donating intents helps the system predict future actions and improve the overall system experience. Don’t donate app intents that the system creates and asks you to handle.

## Parameters

- `result`: The effective result of the intent. Use this parameter to specify the result your intent would have returned. For example, if the action opened another item, include a result with a related [`OpenIntent`](openintent.md) type.

## See Also

- [func donate() async throws -> IntentDonationIdentifier](appintent/donate-1e60c.md)
  Donates the app intent to the system asynchronously.
- [func donate() -> IntentDonationIdentifier](appintent/donate-jp6k.md)
  Donates the app intent to the system.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](appintent/donate(result:)-9b25i.md)
  Donates the app intent and a result to the system asynchronously.
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](appintent/callasfunction(donate:)-3qvbt.md)
  Runs the intent’s action after resolving any parameters, returns the resulting value, and optionally donates the intent to the system.
- [func callAsFunction(donate: Bool) async throws](appintent/callasfunction(donate:)-7v1om.md)
  Runs the intent’s action after resolving any parameters, and optionally donates the intent to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/donate(result:)-36cia)*