# callAsFunction(donate:)

**Framework**: App Intents  
**Kind**: method

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
func callAsFunction(donate donateOnCompletion: Bool = true) async throws where Self.PerformResult.Value == Never
```

## See Also

- [func donate() async throws -> IntentDonationIdentifier](appintent/donate-1e60c.md)
  Donates the intent to the transcript.
- [func donate() -> IntentDonationIdentifier](appintent/donate-jp6k.md)
  Donates the intent to the transcript.
- [func donate(result: some IntentResult) async throws -> IntentDonationIdentifier](appintent/donate(result:)-36cia.md)
  Donates the intent and optional result to the transcript.
- [func donate(result: some IntentResult) -> IntentDonationIdentifier](appintent/donate(result:)-9b25i.md)
  Donates the intent and optional result to the transcript.
- [func callAsFunction(donate: Bool) async throws -> Self.PerformResult.Value](appintent/callasfunction(donate:)-3qvbt.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/callasfunction(donate:)-7v1om)*