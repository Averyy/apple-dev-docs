# donate()

**Framework**: App Intents  
**Kind**: method

Donates the app intent to the system asynchronously.

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
func donate() async throws -> IntentDonationIdentifier
```

## Mentions

- [Donating your app’s data and actions to the system](donating-your-apps-data-and-actions-to-the-system.md)

#### Return Value

An opaque identifier you can use to manage the donation later using an [`IntentDonationManager`](intentdonationmanager.md) type.

#### Discussion

When someone interacts with your app’s interface, create an app intent for the interaction and call this method. Donating intents helps the system predict future actions and improve the overall system experience. Don’t donate app intents that the system creates and asks you to handle.

## See Also

- [func donate() -> IntentDonationIdentifier](appintent/donate-jp6k.md)
  Donates the app intent to the system.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](appintent/donate(result:)-36cia.md)
  Donates the app intent and a result to the system asynchronously.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](appintent/donate(result:)-9b25i.md)
  Donates the app intent and a result to the system asynchronously.
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](appintent/callasfunction(donate:)-3qvbt.md)
  Runs the intent’s action after resolving any parameters, returns the resulting value, and optionally donates the intent to the system.
- [func callAsFunction(donate: Bool) async throws](appintent/callasfunction(donate:)-7v1om.md)
  Runs the intent’s action after resolving any parameters, and optionally donates the intent to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/donate()-1e60c)*