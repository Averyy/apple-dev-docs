# donate()

**Framework**: App Intents  
**Kind**: method

Donates the app intent to the system.

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
func donate() -> IntentDonationIdentifier
```

#### Return Value

An opaque identifier you can use to manage the donation later using an [`IntentDonationManager`](intentdonationmanager.md) type.

#### Discussion

When someone interacts with your app’s interface, create an app intent for the interaction and call this method. Donating intents helps the system predict future actions and improve the overall system experience. Don’t donate app intents that the system creates and asks you to handle.

Call this method to donate the intent synchronously, which you might do if you’re not using Swift concurrency. The system ignores any exceptions it encounters during the donation process.

## See Also

- [func donate() async throws -> IntentDonationIdentifier](appintent/donate-1e60c.md)
  Donates the app intent to the system asynchronously.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](appintent/donate(result:)-36cia.md)
  Donates the app intent and a result to the system asynchronously.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](appintent/donate(result:)-9b25i.md)
  Donates the app intent and a result to the system asynchronously.
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](appintent/callasfunction(donate:)-3qvbt.md)
  Runs the intent’s action after resolving any parameters, returns the resulting value, and optionally donates the intent to the system.
- [func callAsFunction(donate: Bool) async throws](appintent/callasfunction(donate:)-7v1om.md)
  Runs the intent’s action after resolving any parameters, and optionally donates the intent to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/donate()-jp6k)*