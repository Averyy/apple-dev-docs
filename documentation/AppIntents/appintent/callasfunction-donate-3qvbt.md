# callAsFunction(donate:)

**Framework**: App Intents  
**Kind**: method

Runs the intent’s action after resolving any parameters, returns the resulting value, and optionally donates the intent to the system.

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
func callAsFunction(donate donateOnCompletion: Bool = true) async throws -> Self.PerformResult.Value where Self.PerformResult : ReturnsValue
```

#### Return Value

The value the action returns, if any.

#### Discussion

Call this method when you want to perform the current app intent’s action. For example, you might call this method if you use your app intent types to implement your app’s underlying features. This method resolves the parameters of the intent, calls its [`perform()`](appintent/perform().md) method, and returns the resulting value.

## Parameters

- `donateOnCompletion`: `true` if you want to donate the intent to the system after performing the action.

## See Also

- [func donate() async throws -> IntentDonationIdentifier](appintent/donate-1e60c.md)
  Donates the app intent to the system asynchronously.
- [func donate() -> IntentDonationIdentifier](appintent/donate-jp6k.md)
  Donates the app intent to the system.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](appintent/donate(result:)-36cia.md)
  Donates the app intent and a result to the system asynchronously.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](appintent/donate(result:)-9b25i.md)
  Donates the app intent and a result to the system asynchronously.
- [func callAsFunction(donate: Bool) async throws](appintent/callasfunction(donate:)-7v1om.md)
  Runs the intent’s action after resolving any parameters, and optionally donates the intent to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/callasfunction(donate:)-3qvbt)*